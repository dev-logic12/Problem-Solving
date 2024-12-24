def solution(myString):
    answer = ''.join(['l' if ord(i) < ord('l') else i for i in myString])
    return answer