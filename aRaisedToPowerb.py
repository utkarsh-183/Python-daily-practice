
# print("a raised to the power b is : ", a**b)  using exponent inbuilt 

def power(a, b):
    if b == 0:
        return 1
    return a * power(a,b-1)

a = int(input("Enter base Number : "))
b = int(input("Enter Exponential Number : "))
print("a raised to the power b is : ", power(a,b))