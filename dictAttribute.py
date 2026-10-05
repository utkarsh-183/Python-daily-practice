# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.version = 1

# p = Person("Raman", 31)
# print(p.__dict__) 

# ==========================================
# 1. dict()
# ==========================================

# dict() is used to create a dictionary
student = dict(name="Utkarsh", age=19, branch="CSE")

print(student)

# Accessing a value using its key
print(student["name"])

# Adding a new key-value pair
student["college"] = "ABES"

print(student)


# ==========================================
# 2. help()
# ==========================================

# help() gives information about a Python
# function, class, object, or module

help(str)

# You can also get help about a specific method
help(str.upper)

# Help about dictionaries
help(dict)

# Help about a specific dictionary method
help(dict.get)