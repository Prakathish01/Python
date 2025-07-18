# Python writing files (.txt, .json, .csv)
"""
JSON -> Java script object notation
CSV  -> Comma Separated Values
"""

import json
import csv

#---------------------------------------------
txt_data = "This is temporary text file"
json_data = {
    "name" : "sukumar",
    "age"  : 38,
    "native" : "Mayiladuthurai"
}
csv_data = [["Name","Age","Taluk"],
            ["Gandhi",76,"Erode"],
            ["Nehru",67,"CBE"]]
#----------------------------------------------

file_path = "Ex58a_fileWriting.txt"
json_file_path = "Ex58b_fileWriting.json"
csv_file_path = "Ex58c_fileWriting.csv"

# Text file
with open(file_path, "w") as file:
    file.write(txt_data)
    print("Text file created and executed")
with open(file_path, "a") as file:
    file.write("\n" + txt_data)

# JSON file
with open(json_file_path, "w") as jsfile:
    json.dump(json_data, jsfile, indent=4)
    print("JSON file created and executed")

# CSV file
with open(csv_file_path, "w", newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(csv_data)
    print("CSV file created and executed")

