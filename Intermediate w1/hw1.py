class Mixin:
    @staticmethod
    def sub(val1, val2):
        if val1.den == val2.den:
            new_num = val1.num - val2.num
            new_den = val1.den
        else:
            new_num = val1.num * val2.den - val1.den * val2.num
            new_den = val1.den * val2.den
        return Fraction(new_num, new_den)

    @staticmethod
    def add(val1, val2):
        if val1.den == val2.den:
            new_num = val1.num + val2.num
            new_den = val1.den
        else:
            new_num = val1.num * val2.den + val1.den * val2.num
            new_den = val1.den * val2.den
        return Fraction(new_num, new_den)

    @staticmethod
    def mul(val1, val2):
        return Fraction(val1.num * val2.num, val1.den * val2.den)

    @staticmethod
    def truediv(val1, val2):
        return Fraction(val1.num * val2.den, val1.den * val2.num)


class Fraction(Mixin):
    def __init__(self, num, den):
        self.num = self.chek(num)
        self.den = self.chek_den(den)

    @staticmethod
    def chek(x):
        if type(x) != int:
            raise Exception("Числа должны быть целым")
        return x

    @staticmethod
    def chek_den(y):
        if isinstance(y, int) and y != 0:
            return y
        else:
            raise Exception("Числа должны быть целым и больше нуля")

    @property
    def num(self):
        return self.num

    @num.setter
    def num(self, num):
        self.num = self.chek(num)

    @num.deleter
    def num(self):
        del self.num

    @property
    def den(self):
        return self.den

    @den.setter
    def den(self, den):
        self.den = self.chek_den(den)

    @den.deleter
    def den(self):
        del self.den

    def __sub__(self, other):
        if self.den == other.den:
            new_num = self.num - other.num
            new_den = self.den
        else:
            new_num = self.num * other.den - self.den * other.num
            new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __add__(self, other):
        if self.den == other.den:
            new_num = self.num + other.num
            new_den = self.den
        else:
            new_num = self.num * other.den + self.den * other.num
            new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __mul__(self, other):
        return Fraction(self.num * other.num, self.den * other.den)

    def __truediv__(self, other):
        return Fraction(self.num * other.den, self.den * other.num)

    @classmethod
    def string(cls, st):
        st = st.split('/')
        num = st[0]
        den = st[1]
        return cls(num, den)

    def __str__(self):
        return f"{self.num}/{self.den}"


f1 = Fraction(2, 3)
f1.num = 10
f2 = Fraction(5, 4)
f2.den = 8
print(f1 - f2)
print(f1 + f2)
print(f1 * f2)
print(f1 / f2)
print(Fraction.add(f1, f2))
print(Fraction.sub(f1, f2))
print(Fraction.mul(f1, f2))
print(Fraction.truediv(f1, f2))
