def solution(n):
    ls = list(str(int(n)))
    ls.sort(reverse = True)
    print(ls)
    return int("".join(ls))