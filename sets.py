# ==========================================
#              PYTHON SETS
# ==========================================

# A set is a collection of unique values.
# Duplicate values are automatically removed.

info = {"paneer", "Badwa simla Mirch", "rajma", "183", "paneer"}

print(info)
# "paneer" appears only once because sets don't allow duplicates.


# ==========================================
# 1. Creating a Set
# ==========================================

fruits = {"apple", "banana", "mango"}

print(fruits)


# ==========================================
# 2. Empty Set
# ==========================================

# {} creates an empty dictionary, NOT an empty set.

empty_set = set()

print(empty_set)


# ==========================================
# 3. Adding an Element
# ==========================================

fruits.add("orange")

print(fruits)


# ==========================================
# 4. Adding Duplicate Element
# ==========================================

fruits.add("apple")

# "apple" will not be added again.
# Sets contain only unique values.

print(fruits)


# ==========================================
# 5. Removing an Element
# ==========================================

fruits.remove("banana")

print(fruits)


# ==========================================
# 6. discard()
# ==========================================

# discard() removes an element if it exists.
# It does NOT give an error if the element doesn't exist.

fruits.discard("grapes")

print(fruits)


# ==========================================
# 7. Checking if Element Exists
# ==========================================

if "apple" in fruits:
    print("Apple is present")


# ==========================================
# 8. Length of Set
# ==========================================

print(len(fruits))


# ==========================================
# 9. Loop through a Set
# ==========================================

for fruit in fruits:
    print(fruit)


# ==========================================
# 10. Union
# ==========================================

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# Union gives all elements from both sets.

print(a | b)

# Another way:
print(a.union(b))


# ==========================================
# 11. Intersection
# ==========================================

# Intersection gives common elements.

print(a & b)

# Another way:
print(a.intersection(b))


# ==========================================
# 12. Difference
# ==========================================

# Elements present in a but NOT in b.

print(a - b)

# Another way:
print(a.difference(b))


# ==========================================
# 13. Symmetric Difference
# ==========================================

# Gives elements that are NOT common.

print(a ^ b)

# Another way:
print(a.symmetric_difference(b))


# ==========================================
# 14. Update a Set
# ==========================================

numbers = {1, 2, 3}

numbers.update({4, 5, 6})

print(numbers)


# ==========================================
# 15. Clear a Set
# ==========================================

numbers.clear()

print(numbers)
# Output: set()


# ==========================================
# IMPORTANT
# ==========================================

# Sets:
# 1. Store unique values
# 2. Are unordered
# 3. Do not support indexing
# 4. Are mutable
# 5. Allow different data types

example = {10, "hello", 3.14, True}

print(example)