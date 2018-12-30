# write a class to add 2 nums and return it
# https://docs.python.org/3.5/tutorial/classes.html

class Calculator(object):
    # constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y
    # instance method
    def sum_it(self):
        total = 0
        print("Added two numbers...")
        total = self.x + self.y
        return total

    def sub_it(self):
        sub = 0
        sub = self.x - self.y
        return sub

x, y = 1, 5
# initalize the class
calc = Calculator(x,y)
# run instance method
tot = calc.sum_it()
print(tot)