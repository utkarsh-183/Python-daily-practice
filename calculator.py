a = int(input("Enter first number : "))
b = int(input("Enter second number : "))

print("Sum of both number is : ", a+b)
print("Differnce of both number is : ", abs(a-b))
print("Multiplication of both number is : ", a*b)

if(b==0):
    print("Division by 0 is not possible")
else:
    print("division of both number is : ", a/b)