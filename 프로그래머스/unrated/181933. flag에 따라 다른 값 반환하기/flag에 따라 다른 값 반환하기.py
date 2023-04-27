# //a.startswith('I')
def solution(a, b, flag):
    if str(flag).startswith('T') == True:
        return a+b
    else:
        return a-b
