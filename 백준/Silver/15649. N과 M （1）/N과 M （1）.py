from itertools import permutations 

n,m = map(int, input().split())
lst = list(map(str, range(1, n+1)))

for i in permutations(lst, m):
    print(' '.join(i))