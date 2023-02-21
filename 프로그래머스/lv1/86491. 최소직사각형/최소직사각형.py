def solution(sizes):
  small = []
  big = []
  for i in range(len(sizes)):
    if sizes[i][0] >= sizes[i][1]:
      big.append(sizes[i][0])
      small.append(sizes[i][1])
    else:
      big.append(sizes[i][1])
      small.append(sizes[i][0])
  big.sort(reverse=True)
  small.sort(reverse=True)
  answer = int(big[0]*small[0])
  return answer
