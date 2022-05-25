# class Location:
#     def __init__(self, latitude, longitude):
#         self.latitude = latitude
#         self.longitude = longitude
#
#     def __repr__(self):
#         return f"Location(Latitude={self.latitude}, longitude={self.longitude})"
#
#     def __str__(self):
#         return f"({self.latitude}, {self.longitude})"
#
# bham_academy = Location(52.488647, -1.887249)
# print(bham_academy)

class dog:
    def __init__(self, age):
        self.age = age

    def __str__(self):
        return f"A {self.age} year old dog"

    def __format__(self, format_spec):
        if format_spec == "dog":
            return f"A {self.age * 7} dog-years Dog"
        else:
            return self.__str__()


Bill = dog(3)
print(f"Fido is {Bill:dog}")




