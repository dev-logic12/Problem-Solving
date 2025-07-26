def solution(n, s, l): 
    return [l[:s[1]+1], l[s[0]:], l[s[0]:s[1]+1], l[s[0]:s[1]+1:s[2]]][n-1]
