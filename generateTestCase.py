import json
import uuid


data = []
limit = input("Input Max Test Case: ")
for i in range(0, int(limit)):
    data.append(str(uuid.uuid4()))
with open("example.json", 'w') as jsonFile:
    json.dump({"data":data}, jsonFile, sort_keys=False, indent=4)
    jsonFile.close()
