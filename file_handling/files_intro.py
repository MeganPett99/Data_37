# with open("drink_order.txt") as file:
#     raw_orders = file.readlines()
#     orders = list(map(lambda x: x.strip('\n'), raw_orders))
#
# print(orders, type(orders))

# file.close()

# try:
#     file = open("drink_order.txt")
# except FileNotFoundError as errmsg:
#     print("File has not been found")
#     print(errmsg)
#     raise
colours = ["red\n", "blue\n", "purple\n"]
with open("drink_order.txt", "a") as file:
    file.write("new string to write\n")
    file.writelines(colours)