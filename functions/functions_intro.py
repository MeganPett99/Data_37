# print()
# input()
# type()
# DRY - DON'T REPEAT YOURSELF


# function definition
# def greeting(name="...you!"):
#     return "Hello " + name
#
#
# print(greeting())
# print(greeting("Megan"))

# call the function
# result = greeting("Megan")
# greeting("Shah")
# greeting("Emma")
# print(result)
#
#
# def addition(x, y ):
#     return x + y


# def multiargs(*args):
#     print(args, type(args))
#     for arg in args:
#         print(arg)
#
#
# # list
# def product(num1, *args):
#     produce = num1
#     for x in args:
#         produce *= x
#     return produce
#
#
# print(product(3, 4, 5, 6))


# dictionary
# def kwargs_demo(**kwargs):
#     print(kwargs, type(kwargs))
#
#
# print(kwargs_demo(a="one", b="two"))
#
#
# def calculate_tip(list_of_meals, total_cost, tip_pc):
#     print("you had: ")
#     for meal in list_of_meals:
#         print(meal)
#     print(f"your total is: {total_cost}")
#     print(f"with a {tip_pc: .0%} tip, the total is {total_cost * (1 + tip_pc):.2f}")
#
#
# def calculate_total_cost(*meal_prices, price):
#     total = 0
#     for price in meal_prices.value():
#         total += price
#     return total

def division(denom: int, num: int) -> float:
    return denom / num

a = division(12, 6)

# Good functions
# Name them clearly
# Clear arguments name
# functions that don't Return will return none
# keep them small
# use comments
# consider type hints

