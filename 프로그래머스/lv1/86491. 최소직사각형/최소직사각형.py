def solution(sizes):
    small= []
    big = []
    for size in sizes:
        if size[0] >= size[1]:
            small.append(size[1])
            big.append(size[0])
        else:
            small.append(size[0])
            big.append(size[1])
    
    return max(small) * max(big)
