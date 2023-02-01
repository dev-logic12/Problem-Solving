import sys 
input = sys.stdin.readline

n = int(input())

array = [int(input()) for _ in range(n)]
print("\n".join(map(str, sorted(array))))