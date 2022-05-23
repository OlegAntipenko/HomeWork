class Mixin:
    @staticmethod
    def __sub__(self, other):
        return Fraction(self.__num - other.num, self.__den - other.den)

    @staticmethod
    def __add__(self, other):
        return Fraction(self.__num + other.num, self.__den + other.den)

    @staticmethod
    def __mul__(self, other):
        return Fraction(self.__num * other.num, self.__den * other.den)

    @staticmethod
    def __truediv__(self, other):
        return Fraction(self.__num / other.num, self.__den / other.den)


class Fraction(Mixin):
    def __init__(self, num, den):
        self.__num = num
        self.__den = den

    @staticmethod
    def chek(x):
        if type(x) != int:
            raise TypeError("Числа должны быть целым")

    @property
    def num(self):
        return self.__num

    @num.setter
    def num(self, num):
        self.chek(num)
        self.__num = num

    @num.deleter
    def num(self):
        del self.__num

    @property
    def den(self):
        return self.__den

    @den.setter
    def den(self, den):
        self.chek(den)
        self.__den = den

    @den.deleter
    def den(self):
        del self.__den

    def __sub__(self, other):
        return Fraction(self.__num - other.num, self.__den - other.den)

    def __add__(self, other):
        return Fraction(self.__num + other.num, self.__den + other.den)

    def __mul__(self, other):
        return Fraction(self.__num * other.num, self.__den * other.den)

    def __truediv__(self, other):
        return Fraction(self.__num / other.num, self.__den / other.den)

    @classmethod
    def string(cls, st):
        st = cls.st.split('/')
        num = cls.st[0]
        den = cls.st[1]
        return Fraction(num, den)

    def __str__(self):
        return f"{self.num}/{self.den}"


f1 = Fraction(8, 10)
f1.num = 10
f2 = Fraction(5, 4)
f2.den = 8
print(f1 - f2)
print(f1 + f2)
print(f1 * f2)
print(f1 / f2)
