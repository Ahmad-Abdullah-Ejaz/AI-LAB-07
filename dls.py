
# Task A: Find goal node G using DLS, starting from A.

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

        
        print(f"DLS traversal from {start} to {goal}:")
        print(f"Depth Limit: {depth_limit}")

        
        while stack:

            
            vertex, depth, path = stack.pop()

            
            print(vertex, end=" ")

            
            if vertex == goal:
                print(f"\nGoal node '{goal}' reached successfully!")
                print("Final Path:", " -> ".join(path))
                return

            
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

        print(f"\nGoal node '{goal}' not found within depth limit!")





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

# Run DLS with depth limit 2.
g.DLS('A', 'G', 2)
