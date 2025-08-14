def solution(my_string):
    n = len(my_string)
    suffixes = list(range(n))
    suffixes.sort(key=lambda i: my_string[i:])
    return [my_string[i:] for i in suffixes]
