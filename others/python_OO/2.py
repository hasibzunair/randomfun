class Dog:

    kind = 'canine'

    def __init__(self, name):
        self.name = name


d = Dog('Fido')
e = Dog('Buddy')

# d
print(d.name) 
print(d.kind) 
# e
print(e.name) 
print(e.kind)
