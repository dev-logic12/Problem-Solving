n = int(input())
for i in range(1, n+1)[::-1] :  # 1부터 n까지 역순
    print(' '*(n-i) + '*'*(i*2-1))
for i in range(2, n+1):  # 2부터 n까지
    print(' '*(n-i) + '*'*(i*2-1))