
before, after = map(int, input().split())
count = 1 

while after != before:
    count += 1 
    if after == before: 
        break
    tmp = after 
    if after % 10 == 1:
        after //= 10 
    elif after %2 == 0:
        after //= 2
    if tmp == after:
        count = -1
        break
print(count)