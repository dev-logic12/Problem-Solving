def solution(n, info):
    global best_archery, best_score

    # 라이언이 해당 종류의 과녁에서 얻은 점수를 계산하는 함수
    def calculate_score(archery):
        score = 0
        for i in range(11):
            if archery[i] == info[i] == 0:
                continue
            if archery[i] > info[i]:
                score += 10 - i
            else:
                score -= 10 - i
        return score

    # 백트래킹으로 가능한 모든 라이언의 화살 개수 조합을 생성하는 함수
    def dfs(idx, arrows_left, archery):
        global best_archery, best_score
        if idx == -1 and arrows_left:
            return
        if arrows_left == 0:
            score = calculate_score(archery)
            if best_score < score:
                best_archery = archery[:]
                best_score = score
            return
        for i in range(arrows_left, -1, -1):
            archery[idx] = i
            dfs(idx-1, arrows_left-i, archery)
            archery[idx] = 0

    # 최고 점수를 가지는 조합을 찾기 위한 초기화
    best_archery = [0 for _ in range(11)]
    best_score = 0

    # dfs 함수 호출
    dfs(10, n, [0 for _ in range(11)])

    # 결과 반환
    return best_archery if best_score != 0 else [-1]
