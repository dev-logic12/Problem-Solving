#BFS
from collections import deque
#컴퓨터의 개수
n=int(input()) 
#연결선의 개수
v=int(input()) # 연결선 개수
#그래프 초기화 
graph = [[] for i in range(n+1)]
#방문한 컴퓨터인지 표시, 길이가 (n+1)이고 0으로 이루어짐 
visited=[0]*(n+1) 
#그래프 생성
for i in range(v): 
    #연결된 컴퓨터 번호를 각 a, b로 입력을 받음 
    a,b=map(int,input().split())
    #a컴퓨터에 b를 연결
    graph[a]+=[b] 
    #b컴퓨터에 a를 넣음(양방향)
    graph[b]+=[a]
#1번 컴퓨터부터 방문 표시 시작 
visited[1]=1 
#첫 번째 컴퓨터에 덱을 만듦 
Q=deque([1])
#Q값이 있는 동안 while문 작동됨 
while Q:
    #c에 의해 Q값의 왼쪽의 있는 값이 지워짐 
    c=Q.popleft()
    #현재 컴퓨터와 연결된 노드를 반복
    for nx in graph[c]:
        #아직 방문하지 않았다면 
        if visited[nx]==0:
            #Q에 추가함 
            Q.append(nx)
            #방문 표시 
            visited[nx]=1
#1번 컴퓨터를 제외하고 모든 방문한 컴퓨터 개수 출력 
print(sum(visited)-1)