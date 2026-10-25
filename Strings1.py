# 1. CREATING STRINGS

s1 = 'Hello'
s2 = "Python"
s3 = """Multiline
String"""

print(s1, s2, s3)
print(type(s1))  # <class 'str'>


# 2. STRING INDEXING

s = "PYTHON"

print(s[0])   # P: First character
print(s[1])   # Y: Second character
print(s[-1])  # N: Last character
print(s[-2])  # O: Second-last character


# 3. STRING SLICING
# Syntax: string[start:stop:step]
# Stop index is excluded.

s = "PYTHON"

print(s[0:3])   # PYT
print(s[:4])    # PYTH
print(s[2:])    # THON
print(s[:])     # PYTHON
print(s[::2])   # PTO: Every second character
print(s[::-1])  # NOHTYP: Reverse string
print(s[-4:-1]) # THO


# 4. STRING IMMUTABILITY
# Strings cannot be changed character by character.

s = "Python"

# s[0] = "J"  # TypeError

# Create a new string instead.
s = "J" + s[1:]
print(s)  # Jython


# 5. STRING LENGTH

s = "Python"

print(len(s))          # 6
print(s[len(s) - 1])   # n
print(s[-1])           # n


# 6. STRING CONCATENATION (+)

a = "Hello"
b = "Python"

print(a + " " + b)  # Hello Python


# 7. STRING REPETITION (*)

print("Hi " * 3)  # Hi Hi Hi


# 8. MEMBERSHIP OPERATORS

s = "Python Programming"

print("Python" in s)      # True
print("Java" in s)        # False
print("Java" not in s)    # True


# 9. STRING COMPARISON

print("Python" == "Python")  # True
print("Python" == "python")  # False
print("abc" < "bcd")         # True


# 10. IMPORTANT STRING METHODS

s = "hello python"

print(s.upper())        # HELLO PYTHON
print(s.lower())        # hello python
print(s.capitalize())   # Hello python
print(s.title())        # Hello Python
print(s.swapcase())     # HELLO PYTHON


# 11. REMOVING WHITESPACE

s = "   Python   "

print(s.strip())   # Removes whitespace from both ends
print(s.lstrip())  # Removes whitespace from the left
print(s.rstrip())  # Removes whitespace from the right


# 12. REPLACE METHOD

s = "I like Java"

print(s.replace("Java", "Python"))
# I like Python

s = "apple apple apple"
print(s.replace("apple", "mango", 1))
# mango apple apple


# 13. FIND AND INDEX

s = "hello python"

print(s.find("python"))  # 6
print(s.find("java"))    # -1

print(s.index("python")) # 6

# find() returns -1 if not found.
# index() raises ValueError if not found.


# 14. COUNT METHOD

s = "banana"

print(s.count("a"))    # 3
print(s.count("ana"))  # 1


# 15. STARTSWITH AND ENDSWITH

s = "Python.py"

print(s.startswith("Python"))  # True
print(s.endswith(".py"))       # True


# 16. SPLIT METHOD
# Converts a string into a list.

s = "apple banana mango"

words = s.split()
print(words)
# ['apple', 'banana', 'mango']

s = "apple,banana,mango"

print(s.split(","))
# ['apple', 'banana', 'mango']


# 17. JOIN METHOD
# Combines strings from an iterable into one string.

words = ["Python", "is", "easy"]

print(" ".join(words))  # Python is easy
print("-".join(words))  # Python-is-easy


# 18. CHECKING STRING CONTENT

print("Python".isalpha())    # True
print("12345".isdigit())     # True
print("Python123".isalnum()) # True
print("   ".isspace())       # True
print("python".islower())    # True
print("PYTHON".isupper())    # True
print("Hello World".istitle()) # True


# 19. ITERATING THROUGH A STRING

s = "Python"

for ch in s:
    print(ch)

# Using indexing
for i in range(len(s)):
    print(s[i])


# 20. TAKING STRING INPUT

name = input("Enter your name: ")

print(name)
print(type(name))  # str


# 21. STRING FORMATTING

name = "Utkarsh"
age = 19

# Recommended: f-string
print(f"My name is {name} and I am {age} years old.")

# Using format()
print("My name is {} and I am {} years old.".format(name, age))


# 22. ESCAPE CHARACTERS

print("Hello\nPython")     # New line
print("Hello\tPython")     # Tab
print("It's Python")       # Apostrophe
print("C:\\Users\\Student") # Backslash

# 24. REVERSE A STRING

s = "Python"

print(s[::-1])  # nohtyP


# 25. PALINDROME CHECK

s = "madam"

if s == s[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")


# 26. COUNT VOWELS

s = "Python Programming"
count = 0

for ch in s.lower():
    if ch in "aeiou":
        count += 1

print("Vowels:", count)


# 27. COUNT VOWELS, CONSONANTS, DIGITS AND SPACES

s = "Python 123"
vowels = consonants = digits = spaces = 0

for ch in s.lower():

    if ch in "aeiou":
        vowels += 1

    elif ch.isalpha():
        consonants += 1

    elif ch.isdigit():
        digits += 1

    elif ch.isspace():
        spaces += 1

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Spaces:", spaces)


# 28. COUNT WORDS

s = "Python is easy to learn"

words = s.split()

print("Number of words:", len(words))


# 29. CHARACTER FREQUENCY USING DICTIONARY

s = "banana"
freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

print(freq)
# {'b': 1, 'a': 3, 'n': 2}


# 30. REMOVE DUPLICATE CHARACTERS

s = "programming"
result = ""

for ch in s:
    if ch not in result:
        result += ch

print(result)  # progamin


# 31. ANAGRAM CHECK

s1 = "listen"
s2 = "silent"

if sorted(s1) == sorted(s2):
    print("Anagrams")
else:
    print("Not anagrams")


# 32. FIND THE MOST FREQUENT CHARACTER

s = "banana"
freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

if freq:
    most_common = max(freq, key=freq.get)

    print("Character:", most_common)
    print("Frequency:", freq[most_common])


# 33. CONVERT STRING TO LIST

s = "Python"

characters = list(s)

print(characters)
# ['P', 'y', 't', 'h', 'o', 'n']


# 34. CONVERT LIST TO STRING

characters = ["P", "y", "t", "h", "o", "n"]

s = "".join(characters)

print(s)  # Python


# 35. REVERSE WORD ORDER

s = "Python is very easy"

words = s.split()
result = " ".join(words[::-1])

print(result)
# easy very is Python


# 36. LONGEST WORD IN A SENTENCE

s = "Python programming is interesting"

words = s.split()

if words:
    longest = max(words, key=len)
    print("Longest word:", longest)


# 37. COUNT UPPERCASE AND LOWERCASE LETTERS

s = "PyThOn"
upper = lower = 0

for ch in s:
    if ch.isupper():
        upper += 1

    elif ch.islower():
        lower += 1

print("Uppercase:", upper)
print("Lowercase:", lower)


# 38. CHECK WHETHER ONE STRING IS A ROTATION OF ANOTHER

s1 = "abcd"
s2 = "cdab"

if len(s1) == len(s2) and s2 in (s1 + s1):
    print("Rotation")
else:
    print("Not a rotation")


# 39. FIND THE FIRST NON-REPEATING CHARACTER

s = "aabbcd"

for ch in s:
    if s.count(ch) == 1:
        print("First non-repeating character:", ch)
        break
else:
    print("No non-repeating character found")


# 40. BUILT-IN FUNCTIONS

s = "cab"

print(len(s))      # 3
print(min(s))      # a
print(max(s))      # c
print(sorted(s))   # ['a', 'b', 'c']
print(list(s))     # ['c', 'a', 'b']

print(ord("A"))    # 65
print(chr(65))     # A

print(str(123))    # "123"
