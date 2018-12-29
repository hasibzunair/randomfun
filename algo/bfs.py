'''
Breadth first search
    - Closest member in a graph that match a certain criterion
    - Model problem as a graph(nodes and edges)

App: 
    - Connection between pair of nodes
    - Closest node to a given on that satisfy crit
'''

graph = {}

graph['You'] = ['Elijah', 'Marissa', 'Nikolai', 'Cassidy']
graph['Elijah'] = ['You']
graph['Marissa'] = ['You']
graph['Nikolai'] = ['John', 'Thomas', 'You']
graph['Cassidy'] = ['John', 'You']
graph['John'] = ['Cassidy', 'Nikolai']
graph['Thomas'] = ['Nikolai', 'Mario']
graph['Mario'] = ['Thomas']

#print(graph)

class QueueItem():
    def __init__(self, value, pointer=None):
        self.value = value
        self.pointer = pointer
    
class Queue():
    def __init__(self):
        self.last = None
        self.first = None
        self.length = 0

    def enqueue(self, value):
        item = QueueItem(value, None)
        if self.last:
            self.last.pointer = item
        if not self.first:
            self.first = item
        self.last = item
        self.length += 1

    def dequeue(self):
        if self.first is not None:
            value = self.first.value
            self.first = self.first.pointer
            self.length -= 1
        else:
            value = None
        return value

# init queue
qe = Queue()

# test queue    
'''
qe.enqueue('a')
qe.enqueue('b')
qe.dequeue()
print('First element:', qe.first.value)
print('Last element:', qe.last.value)
print('Queue length:', qe.length)
'''

def has_truck(person):
    if person == 'John':
        return True
    else:
        return False

'''
What the function does?
    - Check closest neighbours first
    - Neighbour of neighbours
    - Make use of graph and queue data struct
    - Keep track of people already checked, to prevent cycles
'''
def bfs(graph):
    # init queue
    queue = Queue()
    for person in graph['You']:
        queue.enqueue(person)
        
    # add people checked in this set
    people_checked = set()
    degree = 0

    while queue.length:

        person = queue.dequeue()

        if has_truck(person):
            return person
        else:
            degree += 1
            people_checked.add(person)
            for next_person in graph[person]:
                # check to prev cycles
                if next_person not in people_checked:
                    queue.enqueue(next_person)


print(bfs(graph))
