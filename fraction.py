def gcd(m,n):
    while m % n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn
    return n

print(gcd(20, 10))



class Fraction(object):
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __str__(self): 
        return f"{str(self.num)} / {self.den}"

    def show(self):
        print(f"{self.num} / {self.den}")

    def __add__(self, otherfraction):
        newnum = self.num * otherfraction.den + self.den * otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum, newden)
        return Fraction(newnum // common, newden // common)

    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum == secondnum


x = Fraction(1, 2)
y = Fraction(2, 3)
print(x + y)
print(x == y)


        