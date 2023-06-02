n = int(input())

answer = 0 
for a in range(1, n+1): #택희 
    for b in range(1, n+1): #영훈
        for c in range(1, n+1): #남규 
            if (a + b + c == n):
                if (c > b+2):
                    if (a%2 ==1):
                        answer += 1
print(answer)