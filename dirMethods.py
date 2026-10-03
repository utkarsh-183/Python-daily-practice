# x = [1,2,3]
# print(dir(x))  # dir return list of all the methods available for an object

# dir() is a built-in Python function
# It shows the attributes and methods available for an object

name = "Utkarsh"

# Display all available methods and attributes of the string
print(dir(name))


# Example of using some methods shown by dir()

# upper() converts the string into uppercase
print(name.upper())

# lower() converts the string into lowercase
print(name.lower())

# capitalize() makes the first letter uppercase
print(name.capitalize())

# find() returns the position of a character
print(name.find("k"))

# replace() replaces one value with another
print(name.replace("Utkarsh", "Python"))