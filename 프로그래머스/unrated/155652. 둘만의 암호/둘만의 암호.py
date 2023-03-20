'''
def solution(s, skip, index):
    answer = ''
    a = 'abcdefghijklmnopqrstuvwxyz'
    for i in skip:
        if i in a:
        a = a.replace(i, '')
    for i in s:
        change a[(a.index(i) + index) % len(a)]
        answer += change 
        
    return answer 
'''

def solution(s, skip, index):
    answer = ''
    a = 'abcdefghijklmnopqrstuvwxyz'
    for i in skip:
        if i in a:
            a = a.replace(i, '')
    for i in s:
        change = a[(a.index(i) + index) % len(a)]
        answer += change
        
    return answer