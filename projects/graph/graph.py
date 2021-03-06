"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        if vertex_id in self.vertices:
            IndexError('This vertex already exits.')
        else:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            ValueError('This vertex does not yet exist.')

    def get_neighbors(self, vertex_id):
        if vertex_id in self.vertices:
            neigbors = self.vertices[vertex_id]
            return neigbors
        else:
            return None

    def bft(self, starting_vertex):
        # Create a queue
        q = Queue()
        # Create a visited set
        visited = set()
        # Enqueue starting vertex
        q.enqueue(starting_vertex)
        # While queue has length:
        while q.size() > 0:
            # dequeue to temp variable
            temp_item = q.dequeue()
            # Check to see if item in temp var is in visited...if not:
            if temp_item not in visited:
                # print temp variable
                print(temp_item)
                # add to visited
                visited.add(temp_item)
                # loop through neighbours of temp variable and enqueue
                for neighbor in self.get_neighbors(temp_item):
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        # Create a stack
        s = Stack()
        # Create a visited set
        visited = set()
        # push starting vertex
        s.push(starting_vertex)
        # While stack has length:
        while s.size() > 0:
            # pop to temp variable
            temp_item = s.pop()
            # Check to see if item in temp var is in visited...if not:
            if temp_item not in visited:
                # print temp variable
                print(temp_item)
                # add to visited
                visited.add(temp_item)
                # loop through neighbours of temp variable and enqueue
                for neighbor in self.get_neighbors(temp_item):
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=None):
        if visited is None:
            visited = set()

        s = Stack()

        s.push(starting_vertex)

        while s.size() > 0:
            temp_var = s.pop()

            if temp_var not in visited:
                print(temp_var)
                visited.add(temp_var)

                for neighbor in self.get_neighbors(temp_var):
                    self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        # Initiate queue
        q = Queue()
        # Initiate visited set
        visited = set()
        # Enqueue a LIST (which will be the path), containing the starting vertex
        q.enqueue([starting_vertex])
        # As before, loop through until the queue is empty
        while q.size() > 0:
            # initiate temp var which will hold the dequeued list
            temp_var = q.dequeue()
            # Check last item is not in visited
            if temp_var[-1] not in visited:
                # Check if last item matches destination vertex
                if temp_var[-1] == destination_vertex:
                    # return list
                    return temp_var
                # we add last item to visited
                visited.add(temp_var[-1])
                # get all neighbours of last item
                for neighbor in self.get_neighbors(temp_var[-1]):
                    #  make copy of current path, adding neighbours to it, then enqueue
                    copy = list(temp_var)
                    copy.append(neighbor)
                    q.enqueue(copy)

    def dfs(self, starting_vertex, destination_vertex):
        # Initiate stack
        s = Stack()
        # Initiate visited set
        visited = set()
        # Enqueue a LIST (which will be the path), containing the starting vertex
        s.push([starting_vertex])
        # As before, loop through until the stack is empty
        while s.size() > 0:
            # initiate temp var which will hold the popped list
            temp_var = s.pop()
            # Check last item is not in visited
            if temp_var[-1] not in visited:
                # Check if last item matches destination vertex
                if temp_var[-1] == destination_vertex:
                    # return list
                    return temp_var
                # we add last item to visited
                visited.add(temp_var[-1])
                # get all neighbours of last item
                for neighbor in self.get_neighbors(temp_var[-1]):
                    #  make copy of current path, adding neighbours to it, then push
                    copy = list(temp_var)
                    copy.append(neighbor)
                    s.push(copy)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        if visited is None:
            visited = set()
        if path is None:
            path = []
        
        if starting_vertex not in visited:
            visited.add(starting_vertex)
            new_path = list(path)
            new_path.append(starting_vertex)

            if starting_vertex == destination_vertex:
                return new_path

            for neighbor in self.get_neighbors(starting_vertex):
                path_copy = self.dfs_recursive(neighbor, destination_vertex, visited, new_path)
                if path_copy is not None:
                    return path_copy
        return None



if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    # print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    # graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    # graph.dft(1)
    # graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    # print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    # print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
