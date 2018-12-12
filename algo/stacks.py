'''Stacks:
    - linear data struct
    - 2 end points (a top, a base)
    - LIFO method

Add/remove - O(1)
'''

class Stack(object):

    def __init__(self):
        # items kept here
        self.stack = []
    
    def add(self, item):
        # add to top 
        self.stack.append(item)
    
    def pop(self):
        # pop top monst/lateset elem
        self.stack.pop()

    def peek(self):
        # last element/ top element 
        return self.stack[-1]
    
    def size(self):
        return len(self.stack)


def check_parens(eq, pair=['(', ')']):
    '''Stacks also used for syntax checking; match open close parenthesis(e.g: regex, math eqns)
    '''
    st = Stack()
    matches = True
    for c in eq:
        if c == pair[0]:
            st.add(c)
        elif c == pair[1]:
            if st.size():
                st.pop()
            else:
                matches = False
                break
    
    if not matches and st.size():
        matches == False
    return matches


def dec_to_bin(number):
    st = Stack()
    while number > 0:
        remainder = number % 2
        st.add(remainder)
        number = number // 2
        
    binary = ""
    while st.size():
        binary += str(st.peek())
        st.pop()

    return binary

# init stacks
st = Stack()

# add elem
st.add("a")
st.add("1")
st.add("z")
# see list
print(st.stack)
print(st.size())
st.pop()
print(st.stack)
print(st.size())
print("\n")


eq1 = '(a + b) * (c + d)'
print(check_parens(eq=eq1))
eq2 = '(a + b) * (c + d))'
print(check_parens(eq=eq2))
print("\n")

print(dec_to_bin(3))



