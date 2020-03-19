class Graph():
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, new_vertex):
        if new_vertex not in self.vertices:
            self.vertices[new_vertex] = set()
        else:
            ValueError('Vertex already exists.')

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise KeyError('The vertex does not exist')


class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


def earliest_ancestor(ancestors, starting_node):
    # Initialise graph
    graph = Graph()

    # Loop through tuples adding parent and child as vertices
    for (parent, child) in ancestors:
        if child not in graph.vertices:
            graph.add_vertex(child)
        if parent not in graph.vertices:
            graph.add_vertex(parent)
        
        # Connect child to parent each time 
        graph.add_edge(child, parent)

    
    # Continue with standard bfs traversal

    q = Queue()
    visited = set()

    q.enqueue(starting_node)

    temp = None

    while q.size() > 0:
        temp = q.dequeue()

        if temp not in visited:
            visited.add(temp)
            for neighbor in graph.vertices[temp]:
                q.enqueue(neighbor)
    
    if temp == starting_node:
        return -1
    
    return temp
