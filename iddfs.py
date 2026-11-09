
# Task B: Find goal node G using IDDFS, starting from A.

class Graph:
    def __init__(self):

        self.adj = {}

    def addEdge(self, u, v):
        
        if u not in self.adj:
            self.adj[u] = []

        if v not in self.adj:
            self.adj[v] = []

        
        self.adj[u].append(v)

    
    def DLS(self, start, goal, depth_limit):

        
        stack = [(start, 0, [start])]

        
        visited = []

        
        while stack:

            
            vertex, depth, path = stack.pop()

            
            visited.append(vertex)

            
            if vertex == goal:
                return path, visited

            
            if depth >= depth_limit:
                continue

            
            neighbours = self.adj.get(vertex, [])

            
            i = len(neighbours) - 1

            
            while i >= 0:

                neighbour = neighbours[i]

                
                if neighbour not in path:
                    stack.append(
                        (neighbour, depth + 1, path + [neighbour])
                    )

                i -= 1

        return None, visited

    
    def IDDFS(self, start, goal, max_depth):

        
        for limit in range(max_depth + 1):

            print(f"\nDepth Limit: {limit}")

            
            path, visited = self.DLS(start, goal, limit)

            
            print("Traversal:", " -> ".join(visited))

            
            if path is not None:

                print(f"Goal node '{goal}' reached successfully!")
                print("Final Path:", " -> ".join(path))
                return

        print(f"\nGoal node '{goal}' not found!")






g = Graph()

    
g.addEdge('A', 'B')
g.addEdge('A', 'F')
g.addEdge('A', 'D')
g.addEdge('A', 'E')

    
g.addEdge('B', 'K')
g.addEdge('B', 'J')

    
g.addEdge('K', 'N')
g.addEdge('K', 'M')

    
g.addEdge('D', 'G')

    
g.addEdge('E', 'C')
g.addEdge('E', 'H')
g.addEdge('E', 'I')

    
g.addEdge('I', 'L')

    
g.IDDFS('A', 'G', 3)
