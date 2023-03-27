n = int(input())
answer = list(map(int, input().split()))

a = [1]*n
for i in range(1, n):
    for j in range(i):
        if answer[j] > answer[i]:
            a[i] = max(a[i], a[j]+1)
print(max(a))