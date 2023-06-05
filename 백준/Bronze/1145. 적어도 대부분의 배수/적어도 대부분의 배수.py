a, b, c, d, e = map(int, input().split())

for num in range(1, 100000000):
    count = 0 
    if num%a ==0 : count += 1
    if num%b ==0 : count += 1
    if num%c ==0 : count += 1
    if num%d ==0 : count += 1
    if num%e ==0 : count += 1
    if count >2: 
        print(num)
        break