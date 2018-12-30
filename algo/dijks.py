'''
Dijkstra's algorithm
    - find shortest path in directed or undirected graphs
    - Works with weighted graphs(diff costs or length with its edges)
    - Will not work with -ve weights(use bellman ford algo) 
'''

graph = {'A': {'B': 14, 'C': 9, 'D': 7},
         'B': {'A': 14, 'C': 2, 'F': 9},
         'C': {'A':  9, 'B': 2, 'D': 7, 'E': 11},
         'D': {'A':  7, 'C':10, 'E':15},
         'E': {'C': 11, 'D':15, 'F': 6},
         'F': {'B':  9, 'E': 6}
        }

# cost of B to C connection
# graph['C']['B']    

def dijkstra(graph, start, destination):

    # initialize costs of starting node and its neighbors
    costs = {node: float('inf') for node in graph.keys()}
    costs[start] = 0
    # and use parent_nodes to keep track of the chain of
    # nodes that make up the shortest path
    parent_nodes = {}
    for neighbor in graph[start].keys():
        costs[neighbor] = graph[start][neighbor]
        parent_nodes[neighbor] = start
    
    nodes_checked = set()
    while not len(nodes_checked) == len(graph.keys()):
        
        # get lowest cost node
        min_cost, min_cost_node = float('inf'), None
        for node in costs:
            curr_cost = costs[node]
            if curr_cost < min_cost and node not in nodes_checked:
                min_cost, min_cost_node = curr_cost, node
                
        # check if we can reach any of the lowest cost node's
        # neigbors by going through the lowest cose node
        for neighbor in graph[min_cost_node].keys():
            new_cost = min_cost + graph[min_cost_node][neighbor]
            if new_cost < costs[neighbor]:
                costs[neighbor] = new_cost
                parent_nodes[neighbor] = min_cost_node
                
        # early stopping if we visited the destination
            if neighbor == destination:
                break
        if neighbor == destination:
                break
    
        # add the node to the checked nodes
        nodes_checked.add(min_cost_node)
            
    return costs, parent_nodes


costs, parent_nodes = dijkstra(graph, start='A', destination='F')

print('Costs:', costs)
print('Parent Nodes:', parent_nodes)
