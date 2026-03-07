# What is dictionary?
# Dictionaries are used to store data values in key:value pairs. 
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
# As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
# Keys must be immutable which means keys can be strings, numbers or tuples but not lists.

# Functions and Methods :
# clear() - It removes all items from dictionary.
# copy() - It returns a shallow copy of the dictionary.
# fromkeys() - Create a dictionary from the given sequence.
# get() - Returns value of the given key.
# items() - Returns the list with all dictionary keys with values.
# keys() -  Returns a view object that displays a list of all the keys in the dictionary in order of insertion.
# pop() - Returns and removes the element with the given key.
# popitem() - Returns and removes the item that was last inserted into the dictionary.
# setdefault() - Returns the value of a key if the key is in the dictionary else inserts the key with a value to the dictionary.
# values() - Returns a view object containing all dictionary values, which can be accessed and iterated through efficiently.
# update() - Updates the dictionary with the elements from another dictionary or an iterable of key-value pairs. With this method, 
#            you can include new data or merge it with existing dictionary entries.

# Example 1 :
# d_num = {1, 2, 3, 4, 5}
# d_num1 = {"Name" : "Romil", "Age" : 24, "Gender" : "Male"}
# print(d_num, d_num1)
# print(d_num1["Name"])
# print(d_num1["Age"])

# Example 2 : 
# dict1 = { 1: "Ahmedabad", 2: "Baroda", 3: "Surat"}
# print(dict1)
# dict1 = { 1: "Ahmedabad", 2: "Baroda", 3: "Surat", 5: "Surat", '1': "Mumbai"} #It will overwrite the previous value if keys are same
# print(dict1)
# key1 = dict1.keys()
# print(f"{key1} - {type(key1)}")
# print(f" {dict1.values()}")
# print(f" {dict1.items()}")
# for k,v in dict1.items():
#     print(f" {k} ---> {v} ")
# for k in dict1.keys():
#     print(f" {k} ")
# for v in dict1.values():
#     print(f" {v} ")

# Example 3 :
# dict1 = {
#     101 : ['Romil' , 'Naranpura' , 'Python' , 23000],
#     102 : ['Abhijit' , 'Parimal' , 'DS' , 20000],
#     103 : ['Vishwraj' , 'Dholka' , 'DA' , 25000]
# }
# for k,v in dict1.items():
#     if v[3] > 20000:
#         print(f"{k} : ")
#         for i in v:
#             print(f"\t{i} ")

# Example 4 : Find Total Score with output in tuple.
# dict1 = {
#     101 : ['Romil' , 'Naranpura' , 'Python' , 90 , 99, 87],
#     102 : ['Abhijit' , 'Parimal' , 'DS' , 45 , 56 , 80],
#     103 : ['Vishwraj' , 'Dholka' , 'DA' , 78 , 89 , 93]
# }
# result = [] 
# for k, v in dict1.items():
#     marks = v[3:]  
#     total = sum(marks)  
#     avg = total / 3
#     result.append((k, total, avg))

# result = tuple(result)
# print(result)

# Find total income from sales who have sold over 100 items.
# sales = [ {"product": "Pen", "price": 10, "units_sold": 150},
#     {"product": "Notebook", "price": 50, "units_sold": 90},
#     {"product": "Pencil", "price": 5, "units_sold": 300}
# ]
# total = 0 
# for i in sales:
#     if i['units_sold'] > 100:
#         total = i["units_sold"] * i["price"]
#         print(f" {i["product"]} has of total income of {total}")
        
# Fetch only products whose unit sold are more than 100.
# sales = { 
#     "Pen" : {"product": " Pentonic Pen", "price": 10, "units_sold": 150},
#     "Notebook" : {"product": "DOMS Notebook", "price": 50, "units_sold": 90},
#     "Pencil" : {"product": "DOMS Pencil", "price": 5, "units_sold": 300}
# }
# for k,v in sales.items():
#     if v['units_sold'] > 100:
#         print(f"{k} is the {v["product"]} has unit sold over 100")

# Car dictionary with filteration.
# car_dict = {
# "EV" : 
#     {"Maruti" :
#        { "Baleno": {"Price" : 600000, "Model" : "Smart Hybrid"},
#          "sCross": {"Price" : 1300000, "Model" : "VX Hybrid"},
#          "Swift":  {"Price" : 579000, "Model" : "Hybrid"}
#     },
#     "Hyundai" :
#        { "Tucsun" : {"Price" : 2732000, "Model" : "Plug-in Hybrid"},
#          "Sonata" : {"Price" : 2000000, "Model" : "SEL Hybrid"},
#          "IONIQ 6" : {"Price" : 6500000, "Model" : "IONIQ Hybrid"}
#     },
#     "Kia" :
#        { "Niro" : {"Price" : 1500000, "Model" : "EV6"},
#         "Sorento" : {"Price" : 2500000, "Model" : "EV9"}}
# },
# "Petrol" : 
#     {"Maruti" :
#        { "Baleno": {"Price" : 600000, "Model" : "Smart Hybrid"},
#          "sCross": {"Price" : 1300000, "Model" : "VX Hybrid"},
#          "Swift":  {"Price" : 579000, "Model" : "Hybrid"}
#     },
#     "Hyundai" :
#        { "Tucsun" : {"Price" : 2732000, "Model" : "Plug-in Hybrid"},
#          "Sonata" : {"Price" : 2000000, "Model" : "SEL Hybrid"},
#          "IONIQ 6" : {"Price" : 6500000, "Model" : "IONIQ Hybrid"}
#     },
#     "Kia" :
#        { "Niro" : {"Price" : 1500000, "Model" : "EV6"},
#         "Sorento" : {"Price" : 2500000, "Model" : "EV9"}}
# },
# "Disel" : 
#     {"Maruti" :
#        { "Baleno": {"Price" : 600000, "Model" : "Smart Hybrid"},
#          "sCross": {"Price" : 1300000, "Model" : "VX Hybrid"},
#          "Swift":  {"Price" : 579000, "Model" : "Hybrid"}
#     },
#     "Hyundai" :
#        { "Tucsun" : {"Price" : 2732000, "Model" : "Plug-in Hybrid"},
#          "Sonata" : {"Price" : 2000000, "Model" : "SEL Hybrid"},
#          "IONIQ 6" : {"Price" : 6500000, "Model" : "IONIQ Hybrid"}
#     },
#     "Kia" :
#        { "Niro" : {"Price" : 1500000, "Model" : "EV6"},
#         "Sorento" : {"Price" : 2500000, "Model" : "EV9"}}
# }}
# choice = input("Enter the type of car (EV/Petrol/Disel) or specific Brand or put specific Model or 'all' to see all: ")
# match choice:
#    case 'EV' | 'Petrol' | 'Disel':
#        for brand, models in car_dict[choice].items():
#            print(f"\nBrand: {brand}")
#            for model, details in models.items():
#                price = details['Price']
#                model_type = details['Model']
#                print(f" Model: {model}, Price: {price}, Type: {model_type}")
#    case 'Maruti' | 'Hyundai' | 'Kia':
#          for car_type, brands in car_dict.items():
#             if choice in brands:
#                   print(f"\nCar Type: {car_type}")
#                   print(f" Brand: {choice}")
#                   for model, details in brands[choice].items():
#                      price = details['Price']
#                      model_type = details['Model']
#                      print(f"  Model: {model}, Price: {price}, Type: {model_type}")
#    case 'Smart Hybrid' | 'VX Hybrid' | 'Hybrid' | 'Plug-in Hybrid' | 'SEL Hybrid' | 'IONIQ Hybrid' | 'EV6' | 'EV9':
#        for car_type, brands in car_dict.items():
#            for brand, models in brands.items():
#                for model, details in models.items():
#                    if details['Model'] == choice:
#                        price = details['Price']
#                        print(f"\nCar Type: {car_type}")
#                        print(f" Brand: {brand}")
#                        print(f"  Model: {model}, Price: {price}, Type: {choice}")
#    case 'all':
#        for car_type, brands in car_dict.items():
#            print(f"\nCar Type: {car_type}")
#            for brand, models in brands.items():
#                print(f" Brand: {brand}")
#                for model, details in models.items():
#                    price = details['Price']
#                    model_type = details['Model']
#                    print(f"  Model: {model}, Price: {price}, Type: {model_type}")