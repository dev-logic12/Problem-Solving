n = int(input())
a = set(map(int, input().split()))
m = int(input())
arr = list(map(int, input().split()))

for num in arr:
    print(1) if num in a else print(0)