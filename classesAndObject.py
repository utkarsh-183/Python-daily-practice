class Person:
    name = "Utkarsh"
    occupation = "Student"
    networth = 1000

    def info(self):
        print(f"{self.name} is a {self.occupation}")

    def show_networth(self):
        print(f"{self.name}'s net worth is ₹{self.networth}")

    def introduce(self):
        print(f"Hi, I am {self.name}. I am a {self.occupation}.")


a = Person()
a.name = "Virat"
a.occupation = "Cricketer"
a.networth = 150000000

a.info()
a.show_networth()
a.introduce()


b = Person()
b.name = "Pardeep"
b.occupation = "Kabaddi Player"
b.networth = 50000000

b.info()
b.show_networth()
b.introduce()