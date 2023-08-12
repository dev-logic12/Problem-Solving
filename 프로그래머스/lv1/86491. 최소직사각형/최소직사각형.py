def solution(sizes):
    height = 0 
    vertical = 0 
    for h, v in sizes:
        if h < v:
            h, v = v, h
        height = max(height, h)
        vertical = max(vertical, v)
    return height*vertical

