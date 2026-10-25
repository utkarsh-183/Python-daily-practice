# N to 1
def tillN(num) :
    if num==0:
        return 
    tillN(num - 1)
    print(num)

num = int(input("Enter the Number : "))
tillN(num)

# using loop
# for i in range(1, num+1):
#     print(i)
    

# N to 1
def tillN(num) :
    if num==0:
        return 
    print(num)
    tillN(num - 1)

num = int(input("Enter the Number : "))
tillN(num)