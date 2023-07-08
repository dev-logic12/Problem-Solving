def solution(sizes):
    big = 0
    small = 0
    for size in sizes:
        if size[0] >= size[1]: 
            big = max(big, size[0])
            small = max(small, size[1])
        else:
            big = max(big, size[1])
            small = max(small, size[0])
    return big*small
