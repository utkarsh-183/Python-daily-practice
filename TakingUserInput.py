# a = input("Enter your name : ")
# print("Your name is : ", a)

b = input("Enter the value of b : ")
c = input("ENter the value of c : ")


# string conatination
print(b+c)  

# integer addition
print(int(b) + int(c))

# ==========================================
# PYTHON USER INPUT PRACTICE
# ==========================================


# 1. Taking String Input

# a = input("Enter your name : ")
# print("Your name is : ", a)


# ==========================================
# 2. Taking Two Inputs

b = input("Enter the value of b : ")
c = input("Enter the value of c : ")


# ==========================================
# 3. String Concatenation
# input() always takes input as a string.
# + joins two strings.

print("String concatenation : ", b + c)


# ==========================================
# 4. Integer Addition
# int() converts string into integer.

print("Integer addition : ", int(b) + int(c))


# ==========================================
# 5. Integer Subtraction

print("Subtraction : ", int(b) - int(c))


# ==========================================
# 6. Integer Multiplication

print("Multiplication : ", int(b) * int(c))


# ==========================================
# 7. Division
# Division by zero is not allowed.

if int(c) == 0:
    print("Division is not possible by zero")
else:
    print("Division : ", int(b) / int(c))


# ==========================================
# 8. Floor Division
# // gives the floor division result.

if int(c) == 0:
    print("Floor division is not possible by zero")
else:
    print("Floor division : ", int(b) // int(c))


# ==========================================
# 9. Modulus
# % gives the remainder.

if int(c) == 0:
    print("Modulus is not possible by zero")
else:
    print("Remainder : ", int(b) % int(c))


# ==========================================
# 10. Power
# ** calculates power.

print("Power : ", int(b) ** int(c))


# ==========================================
# 11. Check Even or Odd

if int(b) % 2 == 0:
    print("b is even")
else:
    print("b is odd")


# ==========================================
# 12. Check Greater Number

if int(b) > int(c):
    print("b is greater")
elif int(c) > int(b):
    print("c is greater")
else:
    print("Both are equal")


# ==========================================
# 13. Taking Float Input

price = float(input("Enter price : "))

print("Price is : ", price)


# ==========================================
# 14. Taking Multiple Inputs in One Line

x, y = map(int, input("Enter two numbers : ").split())

print("Sum of x and y : ", x + y)


# ==========================================
# 15. Taking List Input

numbers = list(map(int, input("Enter numbers : ").split()))

print("Your list is : ", numbers)


# ==========================================
# END OF USER INPUT PRACTICE
# ==========================================