import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize
num_of_vertices, num_of_edges = map(int, input().split())
start_vertex = int(input())
distance = [INF] * (num_of_vertices + 1)  # 가중치 테이블 dp
heap = []  # 최소 힙
graph = [[] for _ in range(num_of_vertices + 1)]  # 그래프 정보를 담는 리스트

def dijkstra(start):
    distance[start] = 0
    heapq.heappush(heap, (0, start))

    while heap:
        weight, current_vertex = heapq.heappop(heap)

        if distance[current_vertex] < weight:
            continue

        for w, next_vertex in graph[current_vertex]:
            next_weight = w + weight
            if next_weight < distance[next_vertex]:
                distance[next_vertex] = next_weight
                heapq.heappush(heap, (next_weight, next_vertex))

for _ in range(num_of_edges):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))  # (가중치, 목적지 노드) 형태로 그래프 정보 저장

dijkstra(start_vertex)  # 다익스트라 알고리즘 실행

for i in range(1, num_of_vertices + 1):
    print("INF" if distance[i] == INF else distance[i])  # 최단거리 출력