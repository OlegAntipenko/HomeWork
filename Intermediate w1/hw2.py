import math


class Point2D:
    COUNT = 0
    def __init__(self, x, y):
        self.__class__.COUNT += 1
        self.x = x
        self.y = y

    @classmethod
    def get_count(cls):
        return cls.COUNT

    def distance(self, other):
        return math.sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2)


class Point3D(Point2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def distance(self, other):
        return math.sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2 + (other.z - self.z) ** 2)


p1 = Point2D(2, 4)
p2 = Point2D(4, 8)
print(p1.distance(p2))
p3 = Point3D(2, 4, 6)
p4 = Point3D(4, 8, 10)
print(p3.distance(p4))
print(Point2D.get_count())


