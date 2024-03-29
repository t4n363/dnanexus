import os
import random
import string

LINE_SEPARATOR = '\n'

def generate_random_row(row_number):
    # Generate a random string of characters with a length of 1000
    random_characters = ''.join(random.choice(string.ascii_letters) for _ in range(1000))
    # Concatenate the row number at the start and end of the random string, for a future debugging and testing
    return f"{row_number}{random_characters}{row_number}{LINE_SEPARATOR}"

def create_file(folder_path):
    # Check if the folder exists
    if not os.path.exists(folder_path):
        print(f"Folder '{folder_path}' does not exist.")
        return

    # Define the path for the output file
    file_path = os.path.join(folder_path, "test_data.txt")

    # Restrict the maximum file size to 500MB, to save time on generation and indexing
    max_file_size = 500 * 1024 * 1024
    current_size = 0
    row_number = 1

    with open(file_path, 'w', newline='\n' ) as file:
        # Generate rows until the file size reaches the limit
        while current_size < max_file_size:
            row = generate_random_row(row_number)     
            file.write(row)
            current_size += len(row)
            row_number += 1

    print(f"File 'test_data.txt' created successfully at '{file_path}'.")



if __name__ == "__main__":
    folder_path = input("Enter the folder path: ")
    create_file(folder_path)
