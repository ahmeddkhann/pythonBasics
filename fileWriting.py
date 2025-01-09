

#      TEXT FILE


simple_text = "I like pizza!"
pizza_text = "my team likes pizza too"
employes = ["Ahmed", "Morgan", "Jhone", "Patrick", "Squidbob"]

filePath1 = "text.txt"

with open (filePath1, "w") as file:
    file.write(simple_text + "\n")
    file.write(pizza_text + "\n")
    for employe in employes:
        file.write(employe + " ")
   # print(f"{filePath1} is created")


#     JSON FILE
import json

employe = {
    "name": "Ahmed Khan",
    "age": 20,
    "role": "CyberSecurity enthussiast",
    "salary": 1500000
}
file_path2 = "data.json"

with open(file_path2, "w") as file:
    json.dump(employe, file, indent=4)

    #print(f"{file_path} is created")



#     CSV FILE

import csv
workers = [
    ["Name", "Age", "Job"],
    ["Ahmed", 20, "Programmer"],
    ["Patrick", 25, "unemployed"],
    ["Jone", 22, "cook"]
]


file_path3 = "table.csv"
with open (file_path3, "w", newline="") as file:
    writer = csv.writer(file)
    for row in workers:
        writer.writerow(row)
print(f"csv file {file_path3} is created successfully")