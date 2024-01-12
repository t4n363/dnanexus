import os

def build_index(input_file, index_file):
    # Create the offset index
    with open(input_file, 'r', encoding='utf-8') as f_input, open(index_file, 'w', encoding='utf-8') as f_index:
        offset = 0
        # Offset is lenth in bytes to skip before the requested row
        for line in f_input:
            f_index.write(f"{offset}\n")
            offset += len(line.encode('utf-8')) + 1
            # +1 added to point on a next caracter after the end of the row

def get_line(input_file, index_file, line_number):
    with open(index_file, 'r', encoding='utf-8') as f_index:
        offsets = f_index.readlines()
        offset = int(offsets[line_number - 1])  # line_number is 1-indexed
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