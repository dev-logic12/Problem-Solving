def solution(n):
    d = 2
    s = set()
    while d <= n:
        if n % d == 0:
            s.add(d)
            n = n / d
        else:
            d = d + 1
    return sorted(list(s))