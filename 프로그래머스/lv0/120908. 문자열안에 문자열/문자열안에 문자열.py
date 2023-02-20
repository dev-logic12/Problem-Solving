def solution(str1, str2):
  answer = 0 
  for i in range(len(str1)):
    if str2 in str1: 
      return 1 
    else:
      return 2