import sys
ssr = sys.stdin.readline

N = int(ssr())
arr = list(ssr().split())
max_len = len(max(arr, key=lambda x: len(x))) * 2
new_arr = []
for i in range(N):
    new_arr.append([(arr[i] * (max_len // len(arr[i]) + 1))[:max_len], len(arr[i])])
new_arr.sort(key=lambda x: -int(x[0]))
ans = ''
for i in range(N):
    ans += new_arr[i][0][:new_arr[i][1]]
print(int(ans))