# 6. Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt

import string

# Loop through each uppercase letter
for letter in string.ascii_uppercase:  #string.ascii_uppercase constant to generate them automatically
# Create the filename
    filename = letter + ".txt"
# Open the file and write the message
    with open(filename, "w") as file:
         file.write("This is file " + filename)