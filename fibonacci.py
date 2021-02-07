def fib(n):
    if n >= 3:
        return fib(n -1) + fib(n - 2)
    return 1

# result = int(input("enter integer: "))
# print(fib(result))

# **************************************
def fib1(x):
    if x == 0 or x == 1:
        return 1
    return fib(x - 1) + fib(x - 2)

# print(fib1(5))

# a more efficient way to check the fibonacci sequemce is by using a dictionary
# this is a method called memoization

def fib_efficient(num, dict_): # call fib with the value of num plus a dictionary
    if num in dict_: # if it's already computed, just return the value in the dictionary
        return dict_[num]
    else: #otherwise
        answer = fib_efficient(num - 1, dict_) + fib_efficient(num - 2, dict_) #do the computation, store in the dictionary and return answer
        dict_[num] = answer
        return answer

dict_ = {1:1, 2:2}
print(fib_efficient(10, dict_))
