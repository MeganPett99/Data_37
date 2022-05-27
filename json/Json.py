import json

# car_data = {
#     "make": "Tesla",
#     "type": "Electric",
#     "Faults": 8354,
#     "death_trap":True,
#     "driver":None
# }
#
# dumps = json.dumps(car_data)
#
# print(dumps, type(dumps))
#
# with open('tesla.json', 'w') as jsonfile:
#     json.dump(car_data, jsonfile)

with open("spartan.json") as jsonfile:
    spartan = json.load(jsonfile)

print(spartan, type(spartan))