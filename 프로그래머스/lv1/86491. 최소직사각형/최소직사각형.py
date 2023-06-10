def solution(sizes):
    big = []
    small = []
    for size in sizes:
        if size[0] >= size[1]:
            big.append(size[0])
            small.append(size[1])
        else:
            small.append(size[0])
            big.append(size[1])
    return max(small) * max(big)
