import sys

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a < b:
            self.parent[b] = a
        else:
            self.parent[a] = b

n = int(sys.stdin.readline())

# 각 행성들의 좌표를 입력받음
planets = []
for i in range(n):
    x, y, z = map(int, sys.stdin.readline().split())
    planets.append((x, y, z, i))

# 각 좌표별로 x, y, z 축을 기준으로 정렬한 간선들을 만듦
edges = []
for j in range(3):
    planets.sort(key=lambda planet: planet[j])
    for i in range(1, n):
        cost = abs(planets[i][j] - planets[i-1][j])
        edges.append((cost, planets[i][3], planets[i-1][3]))

# 간선을 비용 기준으로 정렬
edges.sort()

uf = UnionFind(n)
result = 0
for edge in edges:
    cost, a, b = edge
    if uf.find(a) != uf.find(b):
        uf.union(a, b)
        result += cost

print(result)
