import sys
input=sys.stdin.readline

T = int(input()) # 테스트 케이스의 수

for _ in range(T) :
    N, M = map(int, input().split()) # 국가의 수 N과 비행기의 종류 M

    # 입력
    for _ in range(M) :
        a, b = map(int, input().split())
    print(N-1)