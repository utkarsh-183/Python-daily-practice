class Player:

    def __init__(self, name, runs, matches):
        self.name = name
        self.runs = runs
        self.matches = matches

    def info(self):
        print(f"{self.name} has scored {self.runs} runs in {self.matches} matches")

    def average(self):
        print(f"{self.name}'s average is {self.runs / self.matches:.2f}")


a = Player("Rohit", 12000, 260)
b = Player("Virat", 15000, 260)

a.info()
a.average()

print()

b.info()
b.average()