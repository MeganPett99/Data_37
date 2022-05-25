class rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.height + self.width)


class square(rectangle):
    def __init__(self):
        super(). __init__(width = 3, height = 3)
        self.width = self.width
        self.width = self.height

    def square_area(self):
        return self.width * self.width

    def square_perimeter(self):
        return 2 * (self.width + self.width)


rect = rectangle(3,5)
area = rect.get_area()
print(area)

sq = square()
are = sq.square_perimeter()
print(are)