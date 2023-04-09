def solution(sizes):
    small = []
    big = []
    for i in range(len(sizes)):
        if sizes[i][0] >= sizes[i][1]:
            small.append(sizes[i][1])
            big.append(sizes[i][0])
        else:
            small.append(sizes[i][0])
            big.append(sizes[i][1])
    return max(small)*max(big)