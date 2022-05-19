shopping_list = ["bread", "apples", "biscuits", "eggs"]

# print(shopping_list[0])
# print(shopping_list[::-1])

shopping_list[0] = "sugar"
print(shopping_list)

shopping_list.append("spam")
print(shopping_list)

shopping_list[4]
print(shopping_list[4])

shopping_list.remove("spam")
print(shopping_list)

print(shopping_list.pop())
print(shopping_list)

mixed_list = [1, 5, 8, 10j, "lol", True, False]
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(nested_list)
print(nested_list[1])
print(nested_list[1][-1])