def gcd(m: int, n: int) -> int:
    while m % n != 0:
        old_m = m
        old_n = n

        m = old_n
        n = old_m % old_n
    return n


class Fraction(object):
    def __init__(self, top: int, bottom: int):
        """
        初始化函数
        """
        # attributes
        common = gcd(top, bottom)
        top //= common
        bottom //= common

        self.top = top  # 这是两个东西
        self.bottom = bottom
        self.__test = 1  # private attributes

    def show(self):
        """
        public method
        """
        print(f"{self.top}/{self.bottom}")

    def __str__(self) -> str:
        return str(self.top) + "/" + str(self.bottom)

    def __repr__(self) -> str:
        return str(self.top) + "/" + str(self.bottom)

    def __add__(self, other):
        new_top = self.top * other.bottom + self.bottom * other.top
        new_bottom = self.bottom * other.bottom

        return Fraction(new_top, new_bottom)

    def __mul__(self, other):
        new_top = self.top * other.top
        new_bottom = self.bottom * other.bottom

        return Fraction(new_top, new_bottom)

    def __eq__(self, other) -> bool:
        if (self.top == other.top) and (self.bottom == other.bottom):
            return True
        return False


f1 = Fraction(top=3, bottom=5)
print(f1)
f2 = Fraction(top=6, bottom=10)  # __init__
print(f2)
f3 = f1 + f2  # call __add__
print(f3)
f4 = f1 * f2  # call __mul__
print(f4)  # call __str__
f1 == f2  # call __eq__
