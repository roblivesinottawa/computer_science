# def num_ways(n):
#     n = (n -1) + (n - 2)
#     return n

# print(num_ways(4))

# **********************************


# def num_ways(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return num_ways(n-1) + num_ways(n-2)

# print(num_ways(4))



# *********************************

def num_ways(n):
    if n == 0:
        return 1
    else:
        total = 0
        for x in [1,3,5]:
            if n - x >= 0:
                total += num_ways(n - x)
        return total

print(num_ways(4))