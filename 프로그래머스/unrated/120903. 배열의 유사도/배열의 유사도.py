def solution(s1, s2):
    answer = 0
    C = set(s1) & set(s2)
    D = [i for i in s1 if i in s2]
    return len(D)