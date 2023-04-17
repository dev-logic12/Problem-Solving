import sys 
input_fn = sys.stdin.readline
n, m = map(int, input_fn().split())

idx_to_name = {}
name_to_idx = {}
for i in range(1, n+1):
    name = input_fn().rstrip()
    idx_to_name[i] = name 
    name_to_idx[name] = i

for _ in range(m):
    query = input_fn().rstrip()
    if query.isdigit():
        print(idx_to_name[int(query)])
    else:
        print(name_to_idx[query])
