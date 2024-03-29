# 3. Write a Python program with builtin function that checks whether a passed string is palindrome or not.

def is_palindrome(string):
    string = ''.join(char.lower() for char in string if char.isalnum())  #char.isalnum checks if string is alphanumeric(contains letters and numbers)
    return string == string[::-1] #reverse string

string = input("Enter a string: ")

if is_palindrome(string):
    print(string, "is a palindrome")
else:
        print(string, "is not a palindrome")