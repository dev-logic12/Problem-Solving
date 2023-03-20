n = map(int, input().split())

a = set(map(int, input().split()))
b = set(map(int, input().split()))

res = []
for i in a:
    if i not in b:
        res.append(i)

res.sort()
print(len(res))

if len(res) != 0:
    print(*(res))