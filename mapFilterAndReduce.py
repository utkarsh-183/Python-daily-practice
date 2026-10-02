# # map
# def cube(x):
#     return x*x*x

# print(cube(2))

# l = [1,2,3,4,6,7,9]
# # newl = []
# # for item in l:
# #     newl.append(cube(item))

# newl = list(map(cube, l))
# print(newl)

# # filter
# def filter_function(a):
#     return a>4

# newll = list(filter(filter_function, l))

# print(newll)

# reduce
from functools import reduce
numbers = [1,2,3,4,5]

# calculate sum of number using reduce function

def mysum(x,y):
    return x+y

sum = reduce(mysum, numbers)

print(sum)