# Python reading files(.txt,.json,.csv)

import json,csv

txt_file_path ="Ex59a_fileReading.txt"
json_file_path ="Ex59b_fileReading.json"
csv_file_path ="Ex59c_fileReading.csv"

#Text
print("Text------------------------")
try:
    with open(txt_file_path, "r") as txt_file:
        info = txt_file.read()
        print(info)
except FileNotFoundError:
    print("File not found")

#JSON
print("JSON------------------------")
with open(json_file_path,"r") as json_file:
    content = json.load(json_file)
    print(content)

#CSV
print("CSV-------------------------")
with open(csv_file_path,"r") as csv_file:
    content = csv.reader(csv_file)
    for line in content:
        print(line)