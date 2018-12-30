import time

class this:
    """ a simple class """
    i = 123

    def f(self):
        return "Hello World"

class another:
    def __init__(self, real, imag, counter):
        self.r = real
        self.i = imag
        self.cnt = counter

    def counter(self):
        x = 0
        while x < 5:
            print("Yo yo niggas")
            x += 1
            time.sleep(0.5)

class Dog:

    kind = "canine" # shared by all instances
    
    
    def __init__(self, name):
        self.name = name
        self.tricks = [] # empty list for each doggo
    
    def add_trick(self, trick):
        self.tricks.append(trick)


# a simple generator function 
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]
'''
Pythonic way would be to:
    for char in reverse('golf'):
...     print(char)
'''

# init class
#x = this()
#print(x.i, x.f())

# init class
#x = another(3.0, -4.5, 5)
#print(x.counter, x.counter())

# init class intstance
d = Dog('Lion')
e = Dog('Candy')

print(d.kind, e.kind) # shared by doggos
print("\n")

d.add_trick("Roll Over")
e.add_trick("Play dead")

print(d.name, d.tricks)
print(e.name, e.tricks)