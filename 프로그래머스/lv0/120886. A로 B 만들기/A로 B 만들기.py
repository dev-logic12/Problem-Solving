def solution(before, after):
  answer = sorted(before)
  answer1 = sorted(after)
  if answer == answer1: 
    return 1
  else:
    return 0