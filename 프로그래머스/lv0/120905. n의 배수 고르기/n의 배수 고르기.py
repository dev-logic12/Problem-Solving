def solution(n, numlist):
  answer = []
  for i in range(len(numlist)):
    if numlist[i] % n == 0:
      answer.append(int(numlist[i]))
  return answer