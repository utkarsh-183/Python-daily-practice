# def greet(fx):
#     def mfx():
#         print("Good Morning")
#         fx()
#         print("Thanks for using this function")
#     return mfx

# @greet
# def hello():
#     print("Hello")

# def sum(a,b):
#     print(a+b)

# hello()
# sum(2,3)

def decorator(func):

    def wrapper(name):
        print("Before function")
        func(name)
        print("After function")

    return wrapper


@decorator
def greet(name):
    print(f"Hello {name}")


greet("Utkarsh")