def solution(sizes):
    max_width = 0
    max_height = 0
    
    for size in sizes:
        # 각 사각형의 가로와 세로 중 최댓값과 최솟값을 구함
        width = max(size[0], size[1])
        height = min(size[0], size[1])
        
        # 현재 사각형의 가로와 세로가 기존의 최댓값보다 크다면 갱신
        if width > max_width:
            max_width = width
        # 현재 사각형의 세로가 기존의 최댓값보다 크다면 갱신
        if height > max_height:
            max_height = height
    
    # 최댓값들을 곱하여 최소직사각형의 넓이를 구함
    answer = max_width * max_height
    return answer

