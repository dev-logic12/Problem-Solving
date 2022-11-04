n  = int(input())
num = map(int, input().split())
sosu= 0

for nu in num:
    error = 0
    if nu > 1:
        for i in range(2, nu):
            if nu % i == 0:
                error += 1 
        if error == 0:
            sosu += 1
print(sosu)