import pprint
from string import Template

t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta', 'yellow'], 'blue']]]

#print(t)
#pprint.pprint(t, width = 30)


t = Template("${name} is good at $deed")

x = t.substitute(name = "Hasib", deed= "nothing")
print(x)
