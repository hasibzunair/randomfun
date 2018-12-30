class Greeter(object):

    # constructor
    def __init__(self, name):
        self.name = name # instance variable
    
    # instance method
    def greet(self, loud=False):
        if loud:
            print("HELLO, {}" .format(self.name.upper()))
        
        else:
            print("hello, {}" .format(self.name.lower()))

# make an instance of greeter class
g = Greeter("Fred")
# call instance method
g.greet()
# call instance method and pass argument
g.greet(loud=True)
