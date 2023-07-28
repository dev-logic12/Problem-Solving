def solution(sizes):
    max_length = max_width = 0
    for size in sizes:
        max_length = max(max_length, max(size))
        max_width = max(max_width, min(size))

    return max_length * max_width
