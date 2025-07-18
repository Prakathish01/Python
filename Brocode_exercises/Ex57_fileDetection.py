# Python file detection
# \ - can't use, / -> can use,\\ -> can use

import os # Operating system

file_path = "Ex57a_fileDetection.txt"

if os.path.exists(file_path):
    print("It exists")
    if os.path.isfile(file_path):
        print("Yes its a file")
