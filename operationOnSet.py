# # s1 = {1,2,5,6}
# # s2 = {3,6,7}

# # print(s1.union(s2))

# # print("Print s1 intersection s2 ",s1.intersection(s2))

# # print(s1,s2) # s1 , s2 remain unchanged

# # s1.update(s2)
# # print(s1,s2) # now s1 and s2 changed

# s1 = {"mirzapur", "varanasi", "sonbhadra"}
# s2 = {"jaunpur", "chandauli", "ghazipur", "mirzapur"}

# purvanchal = s1.union(s2)
# print(purvanchal)

# print(purvanchal.symmetric_difference(s2))

# print(s1.isdisjoint(s2))

# s1.remove("sonbhadra")
# print(s1)


# # diff b/w remove and discard remove gives error if not present while discard do not give error

# item = s1.pop()
# print(item)
 
# dictationary in python
# they are ordered collection of key_value pairs that are seperated by commas and enclosed in curly brackets

# dic = {
#     12 : "anshuman",
#     28 : "jatin",
#     50 : "Sharib",
#     63 : "utkarsh"
# }

# print(dic[63])

dic = {"name": "Utkarsh", "age" : 19, "Voting" : True}
print(dic)

print(dic["name"])

print(dic.get("Voting"))

print(dic.keys())

for key in dic.keys():
    print(dic[key])