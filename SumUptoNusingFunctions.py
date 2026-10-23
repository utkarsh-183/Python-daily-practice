
# sum = 0

# for i in range (1,n+1):
#     sum+=i


def sum(n):
    total = 0
    for i in range(1,n+1):
        total+=i
    return total

n1 = int(input("Enter the Number : "))
print("Sum of Numbers till N is : ", sum(n1))

n2 = int(input("Enter the Number : "))
print("Sum of Numbers till N is : ", sum(n2))
