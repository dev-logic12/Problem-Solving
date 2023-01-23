from sys import stdin 

input = stdin.readline
set1 = set()
set2 = set()

n, m = map(int, input().split())
for i in range(n):
    set1.add(input().strip("\n"))
for j in range(n):
    set2.add(input().strip("\n"))
set3 = sorted(list(set1.intersection(set2)))
print(len(set3))
for i in set3:
    print(i)