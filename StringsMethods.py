# Strings are immutable

a = ".......... Raghav .............. Raghav!!"

print(len(a))

# 1. Change case
print(a.upper())
print(a.lower())

# 2. Remove characters from beginning/end
print(a.rstrip("."))       # removes trailing characters
print(a.lstrip("."))       # removes leading characters
print(a.strip("."))        # removes from both sides

# 3. Replace
print(a.replace("Raghav", "Harry"))   # replaces all occurrences

# 4. Split
print(a.split(" "))         # splits the string

# 5. Capitalize
blogHeading = "introduction to PyThOn"
print(blogHeading.capitalize())       # Introduction to python

# 6. Center
str1 = "Welcome to console!!"
print(str1.center(38))

# 7. Count
print(a.count("Raghav"))

# 8. Check ending/starting
print(a.endswith("!!"))
print(a.startswith(".........."))

# 9. Find
print(a.find("!"))          # returns index of first occurrence
print(a.find("Raghav"))

# 10. Index
print(a.index("Raghav"))    # similar to find(), but gives error if not found

# 11. Check if string contains only alphabets
name = "Utkarsh  "
print(name.isalpha())       # False

# 12. Check if string contains only numbers
number = "12345"
print(number.isdigit())     # True

# 13. Check if string contains alphabets and numbers
username = "Utkarsh123"
print(username.isalnum())   # True

# 14. Check lowercase / uppercase
print(name.islower())       # False
print(name.isupper())       # False

# 15. Check if string contains only spaces
space = "   "
print(space.isspace())      # True

# 16. Swap uppercase and lowercase
text = "Hello World"
print(text.swapcase())      # hELLO wORLD

# 17. Title case
text = "welcome to python programming"
print(text.title())         # Welcome To Python Programming

# 18. Join strings
words = ["Python", "is", "easy"]
print(" ".join(words))      # Python is easy

# 19. Check prefix/suffix
print("Python".startswith("Py"))
print("Python".endswith("on"))

# 20. Partition
text = "I love Python"
print(text.partition("love"))

#21. Title
text = "i am eager to learn python"
print(text.title())  # coverts 1st letter of each word to capital