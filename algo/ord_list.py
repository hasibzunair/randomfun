'''
Store items sorted by their values
'''

class SLLNode(object):
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

        
class OrderedList(object):
    def __init__(self, head=None, datatype=int):
        self.head = head
        self.datatype = datatype
        
    def __repr__(self):
        s = ''
        if self.head is not None:
            current_node = self.head
        else:
            current_node = None
        
        while current_node is not None:
            s += ' --> %s' % current_node.data
            current_node = current_node.next_node
        return '\nSize: %s\nData: ' % self.size() + s[5:]
        
    def insert(self, data):
        if not isinstance(data, self.datatype):
            raise AttributeError('New element must have type %s' % self.datatype)
        new_node = SLLNode(data=data, next_node=None)
        
        inserted = False
        
        if self.head is None:
            print('new node')
            self.head = new_node
            inserted = True

        current = self.head
        previous = None
        while current is not None and not inserted:
            if current.data >= new_node.data:
                new_node.next_node = current
                if previous is not None:
                    previous.next_node = new_node
                else:
                    self.head = new_node
                inserted = True
            previous = current
            current = current.next_node
        
        if not inserted:
            previous.next_node = new_node
            new_node.next_node = current
            
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


sll = OrderedList(datatype=int)
print(sll)

sll.insert(data=1)
print(sll)
print(sll.head.next_node)

sll.insert(data=2)
print(sll)
print(sll.head.next_node)

sll.insert(data=2)
print(sll)
sll.insert(data=3)
print(sll)
sll.insert(data=10)
print(sll)
sll.insert(data=10)
print(sll)
sll.insert(data=2)
print(sll)
sll.insert(data=0)
print(sll)
sll.insert(data=1)
print(sll)
sll.insert(data=3)
print(sll)

# search
target = sll.search(data=3)
print(target, target.data)

