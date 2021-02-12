class Coordinate(object):
    # initialize data attributes
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        x_diff_sq = (self.x-other.x) ** 2
        y_diff_sq = (self.y-other.y) ** 2
        return (x_diff_sq + y_diff_sq) ** 0.5
    # name of special method, must return a string
    def __str__(self):
        return f"< x = {str(self.x)}, y = {str(self.y)}>"
        

c = Coordinate(3,4)
zero = Coordinate(0,0)

print(c.distance(zero))
print(c)
print(type(c))
print(isinstance(c, Coordinate))