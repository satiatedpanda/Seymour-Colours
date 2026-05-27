from databaseExtractor import databaseHexExtract
from hexcodeClass import Hexcode

database = databaseHexExtract()
collection_range_database: list[Hexcode] = []
for temphex in database:
    temphex.assign_all_attributes()
    if temphex.inCollectionRange:
        collection_range_database.append(temphex)
del database
del temphex
collection_range_database = sorted(collection_range_database, key=lambda x: x.major_digits)
current = ""
idx = 0
temp_list = []
data = {}

for inex, i in enumerate(collection_range_database):
    if current == i.major_digits:
        temp_list.append(i)
        if inex == len(collection_range_database)-1:
            data[current] = temp_list
        continue
    elif current == "":
        current = i.major_digits
        temp_list.append(i)
        continue 
    tp = temp_list[:]
    data[current] = tp
    temp_list.clear()
    current = i.major_digits
    temp_list.append(i)


del current
del idx
del temp_list


for major in data:
    print(major)
    print(data[major])


# #printing
# for key, value in data.items():
#     print(f"{key}:")
#     for idx, val in enumerate(value):
#         if idx == 0:
#             print(val.hexcode, end=" ")
#         elif (idx+1)%10 == 0:
#             print(val.hexcode)
#         else:
#             print(val.hexcode, end=" ")
#     print("\n")


### UNFINISHED