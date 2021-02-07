def fact(n):
    if n < 2:
        return 1
    return n * fact(n - 1)

result = fact(4)
print(result)

# ********************************************

def fact(n):
    if n >= 1:
        return n * fact(n - 1)
    else: 
        return 1

# result = int(input("enter integer: "))
# print(fact(result))


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(1))


# iterative way

def factor(n):
    num = 1
    for x in range(1, n + 1):
        num *= x
    return num

print(factor(8))