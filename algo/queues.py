'''
Queues:
    - 2 end points (front, end)
    - FIFO method
    - enqueue item -> add to its end
    - dequeue item -> remove it from front

Dis: enqueue or dequeue will have O(n) time comp, since it has
to delete from beginning or insert at beginning of list

** Better way to implement queue is to use a doubly linked list
'''

class Queue(object):

    def __init__(self):
        self.data = []
    
    def enqueue(self, item):
        self.data.insert(0, item)
    
    def dequeue(self):
        return self.data.pop()

    def show_front(self):
        return self.data[-1]

    def show_end(self):
        return self.data[0]


'''
Deque:
    - NOT related to dequeue operation
    - double ended queues
    - add/remove items from both sides of the list

** Time complexity is still O(n)
'''
class Deque(object):
    
    def __init__(self):
        self.data = []
    
    def add_front(self, item):
        self.data.insert(0, item)
        
    def remove_front(self):
        return self.data.pop(0)
        
    def add_end(self, item):
        self.data.append(item)
        
    def remove_end(self):
        return self.data.pop()
    
    def show_front(self):
        return self.data[-1]

    def show_end(self):
        return self.data[0]


# intialize
q = Queue()
# add
q.enqueue(1)
print(q.data)
# add
q.enqueue("a")
print(q.data)
# add
q.enqueue(3)
print(q.data)

# remove
print(q.dequeue())
print(q.data)
# remove
print(q.dequeue())
print(q.data)
print(q.dequeue())
print(q.data)



