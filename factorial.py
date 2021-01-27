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

result = int(input("enter integer: "))
print(fact(result))