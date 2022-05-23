x = 0

while x < 10:
    print(f"while loop running: {x}")
    if x == 5:
        print("yayy! 5!")
    x += 1


# age = input("what is your age?\n")
#
# if int(age) > 15:
#     print("you can see the film")

keep_asking = True
age_int = None
while keep_asking:
    age = input("what is your age?\n")
    if age.isdigit():
        age_int = int(age)
        keep_asking = False
    else:
        print("Please enter a valid number in digits")
print(f"your age is {age_int}")


