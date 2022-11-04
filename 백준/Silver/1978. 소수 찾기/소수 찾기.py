n = int(input())
numbers = map(int, input().split())
count = 0
error = 0

for i in numbers:
    for j in range(2, i):
        if i % j == 0:
            error += 1
            break
        
    if error == 0 and i != 1:
        count += 1 
    error = 0 
print(count)