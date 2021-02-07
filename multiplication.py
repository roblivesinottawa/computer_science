# this is an example of multiplication done in an iterative way

def multiplication(a, b):
    result = 0
    while b > 0:
        result += a
        b -= 1
    return result


print(multiplication(10, 20))


#  recursive solution

def mult(a, b):
    if b == 1:
        return a
    return a + mult(a, b -1)

print(mult(10, 20))


