from collections import defaultdict

class Graph:

    def __init__(self):
        self.Graph = defaultdict(list)

    def addEdge(self,u,v):
        self.Graph[u].append(v)

    def DFS(self,root,visited = set()):
        visited.add(root)
        print(root,end=" ")

        for adjacent in self.Graph[root]:
            if adjacent not in visited:
                self.DFS(adjacent,visited)

if __name__ == "__main__":
    # g = Graph()
    # vertices,edges = input().split()
    # for i in range(int(edges)):
    #     u,v = input().split()
    #     g.addEdge(int(u),int(v))
    # g.BFS(int(input("Enter the starting vertex : ")))
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    g.DFS(2)