def solution(n):
  # 7조각 7사람 1판 
  # 7조각 1사람 1판 
  # 7조각 15사람 3판 
  # n//7 == 0이면 몫을 반환 
  # n//7 아니면 몫+1을 반환 
  if n%7 == 0:
    return n//7 
  else:
    return (n//7)+1   