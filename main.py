import json

with open("lilyvmatt.json", "r") as file:
        data = json.load(file)

print(data)