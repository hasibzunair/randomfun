class Dog:

    #tricks = []  # dont do dis, shared by all instances
    # 1
    def __init__(self, name):
        self.name = name
        #1 --->> empty list for each doggo!
        self.tricks = []

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
d.add_trick("Play dead")
e.add_trick("Roll over")
print(d.tricks)
print(e.tricks)