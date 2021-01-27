def fib(n):
    if n >= 3:
        return fib(n -1) + fib(n - 2)
    return 1

result = int(input("enter integer: "))
print(fib(result))

# **************************************
