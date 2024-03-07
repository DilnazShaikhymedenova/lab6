# 2.Write a Python program to check for access to a specified path. Test the existence, readability, writability and executability of the specified path

import os

def check_path_access(path):
     # Check if the path exists
     if not os.path.exists(path):
         print(f"The path '{path}' does not exist.")
         return

     # Check readability
     if os.access(path, os.R_OK):   #it can be viewed, copied, located 
         print(f"The path '{path}' is readable.")
     else:
         print(f"The path '{path}' is not readable.")

     # Check writability   #it can be changed
     if os.access(path, os.W_OK):
         print(f"The path '{path}' is writable.")
     else:
         print(f"The path '{path}' is not writable.")

     # Check executability   #it can be runed at the terminal
     if os.access(path, os.X_OK):
         print(f"The path '{path}' is executable.")
     else:
         print(f"The path '{path}' is not executable.")

 # Specify the path to check
path = "__pycache__"

# Check access to the specified path
check_path_access(path)