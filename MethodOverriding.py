# class shape:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def area(self):
#         return self.x * self.y

# rec = shape(3,5)
# print(rec.area())

class Circle:
    def __init__(self, r):
        self.r = r

    def area(self):
        return (22*self.r*self.r)/7

circle = Circle(7)
print(circle.area())