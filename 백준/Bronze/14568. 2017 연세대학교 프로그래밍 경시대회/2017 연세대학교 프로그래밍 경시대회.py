n = int(input())
cnt = 0 

for a in range(1, n+1):
    for b in range(1,n+1):
        for c in range(1, n+1):
            if a+b+c == n:
                if c >= b+2:
                    if a%2 == 0:
                        cnt +=1

print(cnt)