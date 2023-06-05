a, b = map(int, input().split())
answer = []
for i in range(-1000, 1001):
    if i*(2*a-i) == b:
        answer = list(set([-i, -(2*a-i)]))
print(*sorted(answer))