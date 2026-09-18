# The conversion of one datatype into another is known as typecasting
a = "1"
b = "2"

print(a + b)
print(int(a) + int(b))

string = "143"
number = 7

print("sum is : ", int(string)+number)

# Implicit type conversion happens automatically by Python
a = 10       # int
b = 2.5      # float

c = a + b

print(c)
print(type(c))

# Explicit type conversion is when we manually convert one data type into another.
a = 100

b = str(a)

print(b)
print(type(b))