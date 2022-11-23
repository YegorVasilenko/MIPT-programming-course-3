from math import pi


class Point:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def set_x(self, x):
        self._x = x

    def set_y(self, y):
        self._y = y

    def __str__(self):
        return "[" + str(self._x) + ", " + str(self._y) + "]"


def dist(a, b):
    return ((b.get_y() - a.get_y()) ** 2 + (b.get_x() - a.get_x()) ** 2) ** 0.5


class Shape:
    def __init__(self, type="Shape"):
        self._type = type

    def __str__(self):
        return str(self._type)


class Circle(Shape):
    def __init__(self, x=0, y=0, radius=1, type="Circle"):
        super().__init__(type)
        self._center_ = Point(x, y)
        self._radius_ = radius

    def __str__(self):
        return " ".join([super().__str__(),
                        self._center_.__str__(),
                        self._radius_.str()])

    def perimeter(self):
        return 2 * pi * self.radius

    def area(self):
        return pi * self.radius**2


class Triangle(Shape):
    def __init__(self, p1, p2, p3, type="Triangle"):
        super().__init__(type)
        self._point_1 = p1
        self._point_2 = p2
        self._point_3 = p3
        self._a_ = dist(p1, p2)
        self._b_ = dist(p2, p3)
        self._c_ = dist(p3, p1)

    def __str__(self):
         return " ".join([super().__str__(), self._point_1.__str__(), self._point_2.__str__(),
                          self._point_3.__str__()])

    def perimeter(self):
        return self._a_ + self._b_ + self._c_

    # Heron's formula
    def area(self):
        s = self.perimeter() / 2
        return (s * (s - self._a_) * (s - self._b_) * (s - self._c_)) ** 0.5


class Rectangle(Shape):
    def __init__(self, p1, p2, p3, p4, type="Rectangle"):
        super().__init__(type)
        self._point_1 = p1
        self._point_2 = p2
        self._point_3 = p3
        self._point_4 = p4
        self._a_ = dist(p1, p2)
        self._b_ = dist(p2, p3)
        self._c_ = dist(p3, p4)
        self._d_ = dist(p4, p1)

    def __str__(self):
         return " ".join([super().__str__(), self._point_1.__str__(), self._point_2.__str__(),
                          self._point_3.__str__(), self._point_4.__str__()])

    def perimeter(self):
        return self._a_ + self._b_ + self._c_ + self._d_

    # Brahmagupta's formula
    def area(self):
        s = self.perimeter() / 2
        return ((s - self._a_) *
                (s - self._b_) *
                (s - self._c_) *
                (s - self._d_)) ** 0.5


class Square(Shape):
    def __init__(self, x=0, y=0, side=1, type="Square"):
        super().__init__(type)
        self._center_ = Point(x, y)
        self._side_ = side
        self._point_1 = Point(self._center_.get_x() + side / 2,
                            self._center_.get_y() + side / 2)
        self._point_2 = Point(self._center_.get_x() + side / 2,
                            self._center_.get_y() - side / 2)
        self._point_3 = Point(self._center_.get_x() - side / 2,
                            self._center_.get_y() - side / 2)
        self._point_4 = Point(self._center_.get_x() - side / 2,
                            self._center_.get_y() + side / 2)

    def __str__(self):
         return " ".join([super().__str__(), self._point_1.__str__(), self._point_2.__str__(),
                          self._point_3.__str__(), self._point_4.__str__()])

    def perimeter(self):
        return 4 * self._side_

    def area(self):
        return self._side_ ** 2


class Rhombus(Shape):
    def __init__(self, x=0, y=0, d_hor=1, d_vert=1, type="Rhombus"):
        super().__init__(type)
        self._center_ = Point(x, y)
        self._d_hor = d_hor
        self._d_ver = d_ver
        side = sqrt((d_hor / 2) ** 2 + (d_ver / 2) ** 2)
        self._side_ = side
        self._point_1 = Point(self._center_.get_x() + side / 2**0.5,
                            self._center_.get_y() + side / 2**0.5)
        self._point_2 = Point(self._center_.get_x() + side / 2**0.5,
                            self._center_.get_y() - side / 2**0.5)
        self._point_3 = Point(self._center_.get_x() - side / 2**0.5,
                            self._center_.get_y() - side / 2**0.5)
        self._point_4 = Point(self._center_.get_x() - side / 2**0.5,
                            self._center_.get_y() + side / 2**0.5)

    def __str__(self):
         return " ".join([super().__str__(), self._point_1.__str__(), self._point_2.__str__(),
                          self._point_3.__str__(), self._point_4.__str__()])

    def perimeter(self):
        return 4 * self._side_

    def area(self):
        return 0.5 * self._d_hor_ * self._d_ver_


a = Triangle(Point(), Point(1, 1), Point(2, 3))
print(a)
