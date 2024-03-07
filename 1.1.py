# BUILTIN FUNCTIONS

# 1. Write a Python program with builtin function to multiply all the numbers in a list


from functools import reduce  #reduce function is used to apply a function to all elements in a list iteratively and return a single result.
numbers = [2, 3, 4, 5]

result = reduce(lambda x, y: x * y, numbers) #lambda is an anonymous function that takes two arguments
print(result)









     








