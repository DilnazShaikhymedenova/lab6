# 2. Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters

string = input("Enter a string: ")

num_upper = sum(1 for char in string if char.isupper())

num_lower = sum(1 for char in string if char.islower())

print("Number of uppercase letters:", num_upper)
print("Number of lowercase letters:", num_lower)