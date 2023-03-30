a, b, c = map(int, [input() for _ in range(3)])
result = str(a * b * c)
count = [0] * 10
for digit in result:
    count[int(digit)] += 1
for cnt in count:
    print(cnt)
