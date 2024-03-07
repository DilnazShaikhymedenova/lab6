# 4. Write a Python program to count the number of lines in a text file.

filename = 'drafttext.txt'
with open(filename, 'r') as file:
    num_lines = 0
    for line in file:
         num_lines += 1

print(f'The number of lines in {filename} is: {num_lines}')
