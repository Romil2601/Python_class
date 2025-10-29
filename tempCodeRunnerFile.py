# city_names = {'ahmedabad' : "" , 'baroda': "" , 'surat' : ""}
# for k in city_names.keys():
#     v = k.upper()
#     city_names[k] = v
# print(city_names)

# city_names = {'ahmedabad' : "" , 'baroda': "" , 'surat' : ""}
# for k in city_names.keys():
#     v = len(k)
#     city_names[k] = v
# print(city_names)

rows = int(input("Enter number of rows for the pyramid pattern: "))
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        if j % 2 == 0:
            print("0", end=" ")
        else:
            print("1", end=" ")
    print()