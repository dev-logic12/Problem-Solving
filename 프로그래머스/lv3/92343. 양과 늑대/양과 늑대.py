def dfs(idx, sheep, wolf, possible):
    global g_info, answer, graph
    
    # 현재 위치에 양이 있다면 sheep 변수를 1 증가
    if g_info[idx] == 0:
        sheep += 1
        answer = max(answer, sheep)
    else: # 현재 위치에 늑대가 있다면 wolf 변수를 1 증가
        wolf += 1
    
    # 만약 늑대의 수가 양의 수보다 많다면 불가능한 경우이므로 종료
    if wolf >= sheep:
        return 
    
    # 현재 위치에서 갈 수 있는 위치들을 possible 리스트에 추가
    possible.extend(graph[idx])
    
    # possible 리스트에 있는 위치들을 dfs 탐색
    for p in possible:
        dfs(p, sheep, wolf, [i for i in possible if i != p])
    
def solution(info, edges):
    global answer, g_info, visited, graph
    answer = 0
    g_info = info
    n = len(info)
    graph = [[] for _ in range(n)]
    
    # 그래프를 만들어주는 과정
    for a, b in edges:
        graph[a].append(b)
        
    # dfs 탐색 시작
    dfs(0, 0, 0, [])
    return answer
