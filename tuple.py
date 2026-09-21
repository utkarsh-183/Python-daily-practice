# tup = (1, 5, 6)
# print(type(tup), tup)

# tup = (1,)
# tup[0] = 90 tuple is not mutable
# print(type(tup), tup)

tup = (1,2,76,32,"green")

print(type(tup), tup)

print(tup[0])
print(tup[1])
print(tup[2])
print(tup[3])
print(tup[4])
# print(tup[10]) out of range

print(len(tup))
print(tup[-2])

if "green" in tup:
    print('Yes green is present in tuple')