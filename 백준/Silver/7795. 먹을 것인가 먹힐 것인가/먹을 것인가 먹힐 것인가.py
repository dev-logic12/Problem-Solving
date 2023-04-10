t = int(input())  # 테스트 케이스의 개수 입력

for _ in range(t):
    n, m = map(int, input().split())  # n과 m 입력
    A = list(map(int, input().split()))  # A 리스트 입력
    B = list(map(int, input().split()))  # B 리스트 입력

    A.sort()  # A 리스트를 오름차순으로 정렬
    B.sort()  # B 리스트를 오름차순으로 정렬

    cnt = 0  # 조건에 맞는 경우의 개수를 저장할 변수

    for i in A:
        # B 리스트에서 i보다 작은 수의 개수를 찾아서 개수를 cnt에 더해줌
        left, right = 0, len(B)
        while left < right:
            mid = (left + right) // 2
            if B[mid] < i:
                left = mid + 1
            else:
                right = mid
        cnt += left

    print(cnt)  # 결과 출력

