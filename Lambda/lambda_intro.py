def add(num1, num2):
    return num1 + num2


print(add(4, 7))

# Lambda functions

addition = lambda num1, num2: num1 + num2

print(addition(4, 7))

# map

savings = [234.00, 555.00, 647.25, 839.00]
bonus = []

for saving in savings:
    bonus.append(saving * 1.1)
print(bonus)


def apply_bonus(saving):
    return  saving * 1.1


bonus_map = list(map(apply_bonus, savings))
print(bonus_map)
for b in bonus_map:
    print(b)


bonus_lambda = list(map(lambda x: x * 1.1, savings))
print(bonus_lambda)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers_lambda = list(map(lambda x: (x ** 2) + 3, numbers))
evens = filter(lambda x: x % 2 == 0, numbers_lambda)
print(list(evens))

jobs = ["Data Analyst", "c# Developer", " Data Engineer", "DevOps Engineer", "Data architect"]
jobs_lambda = filter(lambda x: "Data" in x, jobs)
data_job = map(lambda x: x[5:], jobs_lambda)
print(list(data_job))
