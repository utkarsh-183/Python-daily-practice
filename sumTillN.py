# using loop
# number = int(input("Enter the number : "))
# sum = 0
# for i in range (1, number+1):
#     sum += i
# print(sum)

# using Recursion

def sum(n):
    if n == 1:
        return 1
    return n + sum(n-1)

n = int(input("Enter the number : "))
print(sum(n))