class Point:
    def __init__(self, x, y):
        self.__x = None
        self.__y = None
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if isinstance(x, (int, float)):
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if isinstance(y, (int, float)):
            self.__y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"


class Vector:
    def __init__(self, coordinates: Point):
        self.coordinates = coordinates

    def __setitem__(self, index, value):
        if index == 0:
            self.coordinates.x = value
        elif index == 1:
            self.coordinates.y = value

    def __getitem__(self, index):
        if index == 0:
            return self.coordinates.x
        elif index == 1:
            return self.coordinates.y

    def __call__(self, value=None):
        if value is None:
            return (self.coordinates.x, self.coordinates.y)
        else:
            return (self.coordinates.x * value, self.coordinates.y * value)


    def __str__(self):
        return f"Vector({self.coordinates.x}, {self.coordinates.y})"


# Перевірка роботи класів
vector = Vector(Point(1, 10))

print(vector())      # (1, 10)
print(vector(1))     # (5, 50)