
def solution(n,m):
  answer = 0 
  if n == m == 1:
    return 0
  else:
    return (n-1)+((m-1)*n)
