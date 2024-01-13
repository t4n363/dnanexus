import os
'''
Input file contains only a plain text(assume UTF-8), limited by 1 billion rows, 1000(1 for new line char) charactes per row.
Max size will be 1001 * 1,000,000,000 = 1,001,000,000,000 or ~1TB.
Generated index file would have significant size. 
To avoid read whole file to the memmory and optimize index row seek each line would have fixed size of 13
Index file expected to be ~14GB, 1,000,000,000 * 14 bytes 
'''
def build_index(input_file, index_file):
    # Create the offset index
    with open(input_file, 'r', encoding='utf-8') as f_input, open(index_file, 'w', encoding='utf-8') as f_index:
        offset = 0
        # Offset is lenth in bytes to skip before the requested row
        for line in f_input:
            f_index.write(f"{offset}\n".zfill(14))
            offset += len(line.encode('utf-8')) + 1


def get_line(input_file, index_file, line_number):
    with open(index_file, 'r', encoding='utf-8') as f_index:
        max_lines = os.path.getsize(index_file) // 15
        if line_number <= 0 or line_number > max_lines:  
            return ("Line number is out of range.")
        f_index.seek((line_number-1)*15)
        offset = int(f_index.readline().rstrip('\n'))
        with open(input_file, 'r', encoding='utf-8') as f_input:
            f_input.seek(offset)
            return f_input.readline().rstrip('\n')

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

    line_number = int(sys.argv[2])
    line = get_line(input_file, index_file, line_number)
    print(line)


