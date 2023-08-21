def solution(s):
    return [s[i] for i in range(len(s)) if [s[i]] != s[i+1:i+2]]