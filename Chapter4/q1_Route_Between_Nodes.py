#!/usr/bin/python3

'''
Q4.1
    Route Between Nodes: Given a directed graph, design an algorithm to find out whether there is a route between two nodes.
'''

from Graph import Graph
from Queue import Queue 

#depth first search
def dfs(graph, u, v, visited=None):
    if visited == None:
        visited = set()
    result = False
    for e in graph._outgoing[u]:
        if e in visited:
            continue
        visited.add(e)
        if e == v:
            return True
        result = dfs(graph, e, v, visited)
    #print({e._element for e in visited})
    return result

#breadth first search
def bfs(graph, u, v):
    if u == v:
        return True
    visited = set()
    queue = Queue()
    queue.enqueue(u)

    while not queue.is_empty():
        #print([i._element for i in queue._data if i is not None] )
        for i in range(queue._size):
            u = queue.dequeue()
            visited.add(u)
            for e in graph._outgoing[u]:
                if e in visited:
                    continue
                elif e == v:
                    return True
                queue.enqueue(e)
    return False

#--------TEST--------
def test(graph):
    G = {}
    for i in graph._outgoing.keys():
       G[i._element] = {i2._element for i2 in graph._outgoing[i]}
    print(G)

'''
Graph example
0->1->2->3->4->5
{0: {1}, 1: {2}, 2: {3, 4}, 3: set(), 4: set()}
'''

#make new graph
graph = Graph(True)
V = {}
E = {}
for i in range(9):
    V[i] = graph.insert_vertex(i)
for i in range(6):
    if i == 3:
        E[(i-1,i+1)] = graph.insert_edge(V[i-1],V[i+1])
    elif i == 7:
        continue
    else:
        E[(i,i+1)] = graph.insert_edge(V[i],V[i+1])
    #print("->".join([str(i._element) for i in graph.edges()]))
E[(V[6],V[4])] = graph.insert_edge(V[6],V[4])
E[(V[8],V[1])] = graph.insert_edge(V[8],V[1])
E[(V[2],V[8])] = graph.insert_edge(V[2],V[8])

u = V[2]
v = V[6]
print("-------------")
test(graph)

print("Origin:", u)
#print(dfs(graph, u, v))
print(bfs(graph, u, v))
print("Destination:", v)


