class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if isinstance(value, (int, float)):
            self.__x = value
        else:
            raise ValueError("Invalid value for x, must be a number.")

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if isinstance(value, (int, float)):
            self.__y = value
        else:
            raise ValueError("Invalid value for y, must be a number.")
        
point = Point(5, 10)
print(point.x, point.y)