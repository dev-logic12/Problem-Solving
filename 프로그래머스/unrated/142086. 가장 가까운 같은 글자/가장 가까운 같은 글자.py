def solution(s):
    n = len(s)
    answer = [-1] * n # 초기값으로 -1로 채워진 리스트 생성
    
    # 각 문자를 왼쪽부터 차례대로 탐색하면서 처리
    for i in range(n):
        for j in range(i-1, -1, -1): # i번째 문자보다 왼쪽에 있는 문자들을 탐색
            if s[i] == s[j]:
                answer[i] = i - j
                break
                
    return answer