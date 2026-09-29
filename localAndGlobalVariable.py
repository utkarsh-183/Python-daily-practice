x = 10 # global variable
print(x)

def hello():
    global x # this will change the value of x globally
    x = 5 # local variable
    y = 6
    print(f"local variable is {x}")

hello()
print(f"Global variable is {x}")
# print(y)  this will not work as y is a local variable