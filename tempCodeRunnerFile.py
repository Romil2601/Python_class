import json
data = {'Age': 24, 'Address': 'CG Road'}
with open("file1.json" , "w") as file:
    # data = json.load(file) # ----- Load Method
    json.dump(data, file) # ----- Dump method
    print(" Data entered successfully")