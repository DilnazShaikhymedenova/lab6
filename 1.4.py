# 4. Write a Python program that invoke square root function after specific milliseconds.
# Sample Input:
# 25100
# 2123
# Sample Output:
# Square root of 25100 after 2123 miliseconds is 158.42979517754858


import math 
import time

num = int(input('Enter a number:'))
ms = int(input('Enter the number of milliseconds to wait:'))

time.sleep(ms / 1000)  #sleep stops the function for some milliseconds to execute (divides by 1000 to convert sec to millisec)

sqrt_num = math.sqrt(num)

print(f"Square root of {num} after {ms} milliseconds is {sqrt_num}")