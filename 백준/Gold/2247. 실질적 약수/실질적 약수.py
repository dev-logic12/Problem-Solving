import math

n = int(input())
sqrtn = int(math.sqrt(n) + 0.0000001)
sum = 0

for i in range(2, sqrtn + 1):
    k = n // i
    sum += i * (k - i + 1) + (k - i) * (k + i + 1) // 2
    sum %= 1000000

print(sum)
