# import math   # we can use different math operations
# print(math.floor(4.3432))

# print(math.sqrt(16))

# if we only want to import sqrt
# from math import sqrt as s
# from math import pi
# print(pi)


# result = s(64)
# print(result)

# import math
# print(dir(math))

# Python Math Module Notes
# ========================

import math


# 1. Square Root
print("Square Root:")
print(math.sqrt(16))
print(math.sqrt(25))
print()


# 2. Floor
# Rounds down
print("Floor:")
print(math.floor(4.9))
print(math.floor(4.2))
print()


# 3. Ceil
# Rounds up
print("Ceil:")
print(math.ceil(4.1))
print(math.ceil(4.9))
print()


# 4. Power
print("Power:")
print(math.pow(2, 3))
print(2 ** 3)
print()


# 5. Factorial
print("Factorial:")
print(math.factorial(5))
print()


# 6. GCD
# Greatest Common Divisor
print("GCD:")
print(math.gcd(12, 18))
print(math.gcd(20, 30))
print()


# 7. LCM
# Least Common Multiple
print("LCM:")
print(math.lcm(4, 6))
print(math.lcm(10, 15))
print()


# 8. Pi
print("Value of Pi:")
print(math.pi)
print()


# 9. Euler's Number
print("Value of e:")
print(math.e)
print()


# 10. Integer Square Root
print("Integer Square Root:")
print(math.isqrt(16))
print(math.isqrt(20))
print()


# 11. Absolute Value
# abs() is a built-in Python function
print("Absolute Value:")
print(abs(-10))
print(abs(10))
print()


# 12. Logarithm
print("Logarithm:")
print(math.log(10))
print(math.log(8, 2))
print()


# 13. Log base 10
print("Log Base 10:")
print(math.log10(100))
print(math.log10(1000))
print()


# 14. Sine
# Trigonometric functions use radians
print("Sine:")
print(math.sin(math.pi / 2))
print()


# 15. Cosine
print("Cosine:")
print(math.cos(0))
print()


# 16. Tangent
print("Tangent:")
print(math.tan(0))
print()


# 17. Degrees to Radians
print("Degrees to Radians:")
angle = math.radians(90)
print(angle)
print()


# 18. Radians to Degrees
print("Radians to Degrees:")
angle = math.pi / 2
print(math.degrees(angle))
print()


# 19. isclose()
# Checks whether two numbers are approximately equal
print("isclose:")
print(math.isclose(0.1 + 0.2, 0.3))
print()


# 20. Importing only sqrt
from math import sqrt

print("Using sqrt directly:")
print(sqrt(64))
print()


# 21. Using an alias
from math import sqrt as s

print("Using alias:")
print(s(81))
print()


# 22. Alias for the complete math module
import math as m

print("Using module alias:")
print(m.sqrt(100))
print(m.pi)
print()


# 23. dir()
# Shows the names/functions available inside math
print("Some things available in math module:")
print(dir(math))