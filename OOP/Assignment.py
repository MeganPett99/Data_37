class rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.height + self.width)

    def __str__(self):
        return f" The rectangle has an area of {self.get_area()} and the perimeter is {self.get_perimeter()}"

    def __repr__(self):
        return f"Area: {self.get_area()}, Perimeter: {self.get_perimeter()}"


class square(rectangle):
    def __init__(self):
        super(). __init__(width = 3, height = 3)
        self.width = self.width
        self.width = self.height

    def square_area(self):
        return self.width * self.width

    def square_perimeter(self):
        return 2 * (self.width + self.width)

    def __str__(self):
        return f" The square has an area of {self.square_area()} and the perimeter is {self.square_perimeter()}"

    def __repr__(self):
        return f"Area: {self.square_area()}, Perimeter: {self.square_perimeter()}"

