def solution(myString):
    return ''.join(c if c >= 'l' else 'l' for c in myString)
