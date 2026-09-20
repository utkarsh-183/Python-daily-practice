l = [ 1 , 2 , 4 , 6]
print(l)
l.append(3)
l.append(4)
print(l)
l.sort()
print(l)

l.sort(reverse=True)
print(l)
print(l.index(1))
print(l.count(4))

l.insert(1,899)
print(l)
