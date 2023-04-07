def solution(sizes):
    answer = 0
    small = []
    big = []
    for i in range(len(sizes)):
        small.append(min(sizes[i][0], sizes[i][1]))
        big.append(max(sizes[i][0], sizes[i][1]))
    return max(small) * max(big)
