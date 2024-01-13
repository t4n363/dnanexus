Scripts in the repo:
1. generate_test_data.py
Description:
The script creates a .txt file filled with random character rows, each starting and ending with the iterative row number to check result of the first test task. The generated file is limited to a size below 500MB to reduce time for generation and indexing during development, comparing to file described in the task. For me file generaion takes ~40 minutes.
When script generate_test_data.py executed, it will prompt to provide folder. Choose folder where test data will be stored, and provide full path to it. 

2. search_row_by_index.py - for Problem 1
Description:
Script efficiently retrieves lines from a large text file using an index. The script generates an index file that stores the starting position (offset) of each line in the input file, and it allows you to quickly retrieve any line by specifying its line number.

3. Binary search - for Problem 2
