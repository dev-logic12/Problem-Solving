def solution(sizes):
    row = 0 
    col = 0 
    for r, c in sizes:
        if r < c:
            r, c = c, r 
        row = max(row, r)
        col = max(col, c)
    return row*col
