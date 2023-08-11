def solution(N, number):
    if N == number:
        return 1  # N과 number가 같으면 1번만에 표현 가능

    # 각 숫자마다 가능한 표현 결과를 저장하는 집합의 리스트
    dp = [set() for _ in range(9)]
    for i in range(1, 9):
        dp[i].add(int(str(N) * i))  # 같은 숫자를 i번 사용하는 경우 추가

        for j in range(1, i):
            for num1 in dp[j]:
                for num2 in dp[i - j]:
                    dp[i].add(num1 + num2)
                    dp[i].add(num1 - num2)
                    dp[i].add(num1 * num2)
                    if num2 != 0:
                        dp[i].add(num1 // num2)

        if number in dp[i]:
            return i  # 최소로 사용한 횟수 반환

    return -1  # 8번까지 반복했는데도 number를 만들지 못하면 -1 반환

# 예시 사용
N = 5
number = 12
print(solution(N, number))  # 출력 결과: 4
