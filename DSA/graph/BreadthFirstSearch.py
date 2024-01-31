from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)
    
    def BFS(self,root):

        #mark all the vertices as not visited
        visited = [False]*(max(self.graph)+1)

        #create queue for BFS
        queue = []

        #Mark the source node as visited and enqueue it
        queue.append(root)
        visited[root] = True

        while queue:
            #Dequeue a vertex from queue and print it
            root = queue.pop(0)
            print(root,end=" ")

            """
            Get all adjacent vertices of the dequeued vertex root.
            If an adjacent has not been visited then mark it visited and enqueue it
            """
            for i in self.graph[root]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

if __name__ == '__main__':

    g = Graph()
    vertices,edges = input().split()
    for i in range(int(edges)):
        u,v = input().split()
        g.addEdge(int(u),int(v))
    g.BFS(int(input("Enter the starting vertex : ")))    