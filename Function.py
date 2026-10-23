# function to print Hello world

# def Hello():
#     print("Hello World!!")

# Hello()
# Hello()

# function to add to numbers


# def add(n1,n2):
#     sum=n1+n2
#     return sum

# print("The Sum of two Numbers is : ", add(4,7))

# when we want to take variable number of arguments
# arbitatory arguments
# def add(*args):
#     sum = 0
#     for i in args:
#        sum+=i 
#     return sum

# print("The sum is: ",add(1,3,4,2,5,1))


def StudentInfo(**kwargs):
    for x,y in kwargs.items():
        print(x, "is", y)

StudentInfo(name = "Utksrsh", age = 19, city = "Ghaziabad")
StudentInfo(name = "Anjali", age = 20, city = "Varanasi")