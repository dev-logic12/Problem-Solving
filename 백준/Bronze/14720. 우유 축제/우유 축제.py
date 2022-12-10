n = int(input())
milk_list = list(map(int, input().split()))

#마신 우유를 저장할 변수 
count = 0

for i in range(n):
    if milk_list[i] == count % 3:
        count = count + 1 
print(count)