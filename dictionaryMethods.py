ep1 = {122: 45, 173: 84, 291: 45, 214: 89}
ep2 = {324: 78, 412: 91, 251: 45}

ep1.update(ep2)
# ep1.clear()
ep1.pop(122)
ep1.popitem()
print(ep1)

