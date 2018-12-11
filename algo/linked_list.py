'''
SLL
    - store n elements
    - a node which consists of data and pointer(to next node)
    - can grow in size (if store capacity unknown)
    - insertion at beginning of list is cheap(only change one referenc pointer)

'''

class SLLNode(object):
    def __init__(self, data, next_node = None):
        '''
        Two args:
            - data(that is to be stored)
            - POINTER to next node
        ** next_node is None as last node has no pointer 
        '''     
        self.data = data
        self.next_node = next_node


class SinglyLinkedList(object):
    '''
    __init__, __repr__, insert, size, search, delete
    '''

    def __init__(self, head= None):
        # points to the first node in the data struct
        self.head = head

    def __repr__(self):
        # to make life easy...
        s = ""
        # check is list in empty
        if self.head is not None:
            current_node = self.head
        else:
            current_node = None

        # if list is empty loop not executed
        while current_node is not None:
            s += " --> %s" %current_node.data
            current_node = current_node.next_node
        
        return "\nSize: %s\nData: " %self.size() + s[5:]

    def insert(self, data):
        new_node = SLLNode(data= data, next_node=None)
        new_node.next_node = self.head
        self.head = new_node

    def size(self):
        current_node = self.head
        cnt = 0
        while current_node:
            cnt += 1
            current_node = current_node.next_node
        return cnt

    def search(self, data):
        current_node = self.head
        target_node = None

        while current_node is not None and target_node is None:
            if current_node.data == data:
                target_node = current_node
            else:
                current_node = current_node.next_node
        return target_node

    def delete(self, data):
        current_node = self.head
        previous_node = None
        found = False

        while current_node is not None and not found:
            if current_node.data == data:
                found = True
                if previous_node is None:
                    self.head = current_node.next_node
                else:
                    previous_node.next_node = current_node.next_node
            
            else:
                previous_node = current_node
                current_node = current_node.next_node

# initialize empty linked list
sll = SinglyLinkedList()
print(sll)

# add a node
sll.insert(data=[1, 2, 3])
print(sll)

# add two more node
sll.insert(data=[4, 5, 6])
sll.insert(data=[7, 8, 9])
print(sll)

# search a node
target = sll.search(data=[4, 5, 6])
print(target, target.data)

target = sll.search(data=5)
print(target)

# delete
print('Initial linked list:')
print(sll)
target = sll.delete(data=[4, 5, 6])
print('\nLinked list after deletion:', )
print(sll)

target = sll.delete(data=[7, 8, 9])
print(sll)

# nothig is left :(
target = sll.delete(data=[1,2,3])
print(sll)

