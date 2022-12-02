#이건 dp문제이다 
t = int(input())
def solution(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return solution(n-1) + solution(n-2) + solution(n-3) 
for i in range(t):
    n = int(input())
    print(solution(n))
#1 = 1 -> 1개
#2 = (1+1), 2 -> 2개 
#3 = (1+1+1), (1+2), (2+1), (3) -> 4개 
#4 = (1+1+1+1), (1+1+2), (1+2+1), (1+3), (2+1+1), (2+2), (3+1) -> 7개 
#4번째 경우의 수 = 첫번째+ 두번째+세번째
#5번째 경우의 수 = 2+3+4번째 경우의 수를 합한 것 
#점화식 = (n>3), f(n) = f(n-1)+f(n-2)+f(n-3)