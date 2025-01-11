def solution(myString):
    s = list(myString)
    for i in range(len(s)):
        if ord(s[i]) < ord('l'):
            s[i] = 'l'
    return ''.join(s)