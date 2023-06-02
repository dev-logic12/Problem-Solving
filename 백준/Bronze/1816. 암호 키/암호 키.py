n = int(input())

for _ in range(n):
    obj = int(input())
    for number in range(2, 1000001):
        if (obj % number == 0):
            print('NO')
            break
        if (number == 1000000):
            print('YES')
            break