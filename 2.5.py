# 5. Write a Python program to write a list to a file.

my_list = ["apple", "banana", "cherry", "date"]

# Open a file in write mode
with open("my_list.txt", "w") as file:  #with statement automatically closes the file after the for loop completes, ensuring that all data is written to the file 
# Loop through the list and write each string to a new line in the file
     for item in my_list:
       file.write(item + "\n")  #"\n" ensures that each item is written to a new line in the file.


