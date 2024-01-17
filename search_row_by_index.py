import os
import platform
'''
Input file contains only a plain text(assume UTF-8), limited by 1 billion rows, 1000(1 for new line char) charactes per row.
Max size will be 1001 * 1,000,000,000 = 1,001,000,000,000 or ~1TB.
Generated index file would have significant size. 
To avoid read whole file to the memmory and optimize index row seek each line would have fixed size of 13 digits.
Index file expected to be ~14GB, 1,000,000,000 * 14 bytes.
'''
INDEX_ROW_LEN = 13
LINE_SEPARATOR = '\n'

def build_index(input_file, index_file):
    # Create the offset index
    with open(input_file, 'r', encoding='utf-8') as f_input, open(index_file, 'w', encoding='utf-8', newline=LINE_SEPARATOR) as f_index:
        offset = 0
        # Offset is lenth in bytes to skip before the requested row
        for line in f_input:
            f_index.write(f"{str(offset).zfill(INDEX_ROW_LEN)}{LINE_SEPARATOR}")
            offset += len(line.encode('utf-8')) 

def get_line(input_file, index_file, line_index):
    with open(index_file, 'r', encoding='utf-8', newline=LINE_SEPARATOR) as f_index:
        max_lines = os.path.getsize(index_file) // (INDEX_ROW_LEN + len(LINE_SEPARATOR))
        if line_index < 0 or line_index > max_lines:  
            return ("Line index is out of range.")
        f_index.seek(line_index*(INDEX_ROW_LEN + len(LINE_SEPARATOR)))
        offset = int(f_index.readline().rstrip())
        with open(input_file, 'r', encoding='utf-8', newline=LINE_SEPARATOR) as f_input:
            f_input.seek(offset)
            return f_input.readline().rstrip()

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("Usage example: python search_row_by_index.py input_file_path index")
        sys.exit(1)

    input_file = sys.argv[1]
    index_file = f"{input_file}.index"

    # Check if index file exists, if not, create it
    if not os.path.exists(index_file):
        print("Building index file...")
        build_index(input_file, index_file)
        print("Index file created.")

    line_index = int(sys.argv[2])
    line = get_line(input_file, index_file, line_index)
    print(line)


