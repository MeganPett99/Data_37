class Dog:
    def __init__(self, dog_name, colour):
        self.animal_type = "canine" #class variable
        self.legs = 4
        self.name = dog_name
        self.colour = colour

    def bark(self):  # method
        return f"woof! I am a {self.animal_type}"


bill = Dog("Bill", "brown")
print(bill.animal_type)
print(bill.name)
print(bill.colour)


class Spartan:
    def __init__(self, spartan_name, age):
        self.course_type = "Data_37"
        self.name = spartan_name
        self.age = age

    def greeting(self):
        return f"Hello! {self.name}, you're {self.age} and on {self.course_type}"


Megan = Spartan("Megan", "22")
print(Megan.course_type)
print(Megan.name)
print(Megan.age)


class Car:
    def __init__(self, make, model, top_speed):
        self.car_make = make
        self.car_model = model
        self.car_top_speed = top_speed
        self.__speed = 0

    def accelerate(self, speed_add):
        self.__speed = min(self.__speed + speed_add, self.car_top_speed)

    def brake(self, brake):
        self.__speed = max(self.__speed - brake, 0)

    def get_speed(self):
        return self.__speed


mycar = Car("BMW", "BMW", "160")
mycar.accelerate(150)
mycar.brake(50)





