def solution(n):
    ls = list(sorted(str(n), reverse = True))
    return int("".join(ls))