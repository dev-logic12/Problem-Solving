def solution(strings, n):
  strings.sort()
  return sorted(strings, key=lambda x:x[n]) 
solution(["sun", "bed", "car"], 1)