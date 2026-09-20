# def calculateGmean(a, b):
#     mean = (a*b)/(a+b)
#     print(mean)

# def isGreater(a, b):
#     if(a>b):
#         print("First Number is greater")
#     else:
#         print("Second Number is greater")

# a = 9
# b = 8
# calculateGmean(a, b)
# isGreater(a,b)

# c = 2
# d = 8
# calculateGmean(c, d)
# isGreater(c, d)

# def average(a,b):
#     print("The average is : ", (a+b)/2)

# average(8,9)

# there are 4 types aof arguments in a function

# 1-> default argument
# 2-> keyword Argumnets
# 3-> Variable length Arguments
# 4-> requires Arguments

# def average(*numbers):
#     print(type(numbers))
#     sum = 0
#     for i in numbers:
#         sum = sum + i
#     print("Average is: ", sum/len(numbers))

# average(3,4,5)

# 1. Required Arguments
def add(a, b):
    print("Sum is:", a + b)

add(10, 20)


# 2. Default Arguments
def greet(name="Utkarsh"):
    print("Hello", name)

greet()
greet("Rahul")


# 3. Keyword Arguments
def student(name, age, branch):
    print("Name:", name)
    print("Age:", age)
    print("Branch:", branch)

student(age=19, branch="CSE", name="Utkarsh")


# 4. Variable Length Arguments
def average(*numbers):
    print(type(numbers))
    
    total = 0
    for i in numbers:
        total = total + i
    
    print("Average is:", total / len(numbers))

average(3, 4, 5)
average(10, 20, 30, 40)


# 5. Find Square
def square(n):
    print("Square is:", n * n)

square(5)


# 6. Find Maximum
def maximum(a, b):
    if a > b:
        print(a, "is greater")
    else:
        print(b, "is greater")

maximum(10, 25)


# 7. Check Even or Odd
def evenOdd(n):
    if n % 2 == 0:
        print(n, "is Even")
    else:
        print(n, "is Odd")

evenOdd(7)


# 8. Calculate Factorial
def factorial(n):
    fact = 1
    
    for i in range(1, n + 1):
        fact = fact * i
    
    print("Factorial is:", fact)

factorial(5)


# 9. Calculate GMean
def calculateGmean(a, b):
    gmean = (a * b) / (a + b)
    print("GMean is:", gmean)

calculateGmean(9, 8)


# 10. Return Value
def multiply(a, b):
    return a * b

result = multiply(5, 4)
print("Result:", result)