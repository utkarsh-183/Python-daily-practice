class Student:

    def __init__(self, name, marks):
        self.name = name
        self._marks = marks

    # Getter
    @property
    def marks(self):
        return self._marks

    # Setter
    @marks.setter
    def marks(self, value):
        if value >= 0 and value <= 100:
            self._marks = value
        else:
            print("Invalid marks")


s = Student("Utkarsh", 85)

print(s.marks)      # Getter

s.marks = 90        # Setter
print(s.marks)      # Getter