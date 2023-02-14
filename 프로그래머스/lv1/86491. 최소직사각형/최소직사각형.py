def solution(sizes):

    가로 = []
    세로 = []

    for size in sizes:
        if size[0] >= size[1]:
            가로.append(size[0])
            세로.append(size[1])
        else:
            세로.append(size[0])
            가로.append(size[1])
    
    return max(가로) * max(세로)

