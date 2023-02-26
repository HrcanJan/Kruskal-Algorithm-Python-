 # Read and input file
with open('./Graf_vstup.txt') as f:
    graf = f.readlines()[1:]

with open('./Graf_vstup.txt') as f:
    x = f.readlines()[0]
    x = x.split()
    v = int(x[0])
    h = int(x[1])

# Vrchol 1, Vrchol 2, Vaha
textArray = []
for i in range(h):
    x = graf[i].split()
    x = list(map(int, x))
    textArray.append(x)

# take second element for sort
def takeThird(elem):
    return elem[2]

# sort list with key
textArray.sort(key=takeThird)
for i in textArray:
    i[0] -= 1
    i[1] -= 1

# Credit to: https://www.programiz.com/dsa/kruskal-algorithm
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    # Search function

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def apply_union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    #  Applying Kruskal algorithm
    def kruskal_algo(self):
        result = []
        i, e = 0, 0
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.apply_union(parent, rank, x, y)
        for u, v, weight in result:
            print("%d - %d: %d" % (u, v, weight))

g = Graph(7)
for i in textArray:
    g.add_edge(i[0], i[1], i[2])
g.kruskal_algo()