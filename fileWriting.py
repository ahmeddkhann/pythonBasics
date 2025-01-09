
simple_text = "I like pizza!"
pizza_text = "my team likes pizza too"
employes = ["Ahmed", "Morgan", "Jhone", "Patrick", "Squidbob"]

filePath = "text.txt"

with open (filePath, "w") as file:
    file.write(simple_text + "\n")
    file.write(pizza_text + "\n")
    for employe in employes:
        file.write(employe + " ")
    print(f"{filePath} is created")
