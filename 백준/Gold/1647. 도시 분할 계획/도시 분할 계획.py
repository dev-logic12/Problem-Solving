import sys

# 특정 원소가 속한 집합을 찾기 위한 함수입니다.
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치는 함수입니다.
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 입력을 받습니다.
n, m = map(int, sys.stdin.readline().split())
edges = []
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    edges.append((c, a, b))

# 간선을 가중치를 기준으로 오름차순으로 정렬합니다.
edges.sort()

# 각 집을 독립적인 집합으로 초기화합니다.
parent = [i for i in range(n + 1)]

# 선택한 길로 인해 연결된 두 집합을 하나로 합칩니다.
result = 0
last = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        last = cost  # 마지막으로 선택한 간선의 가중치를 저장합니다.

# 마을을 나누기 위해 하나의 집합으로 합칩니다.
# 마지막으로 선택한 간선을 제외합니다.
print(result - last)
