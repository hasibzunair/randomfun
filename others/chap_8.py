# compound statements
'''
x = 0

while x is not None:
    if x > 50000:
        break
    x += 1
    print(x)

print("I broke! :(")
'''
# errors and exeptions...

while 1:
    try:
        num = int(input("Enter a number: "))
        break
    except ValueError:
        print("A number you fool!")