def solution(sizes):
    max_val = max(sizes[0][0], sizes[0][1])  # sizes 리스트의 첫 번째 요소의 첫 번째와 두 번째 값을 최대값으로 설정합니다.
    min_val = min(sizes[0][0], sizes[0][1])  # sizes 리스트의 첫 번째 요소의 첫 번째와 두 번째 값을 최소값으로 설정합니다.

    for i in range(1, len(sizes)):
        current_max = max(sizes[i][0], sizes[i][1])  # 현재 요소의 첫 번째와 두 번째 값을 비교하여 최대값을 찾습니다.
        current_min = min(sizes[i][0], sizes[i][1])  # 현재 요소의 첫 번째와 두 번째 값을 비교하여 최소값을 찾습니다.

        if current_max > max_val:  # 현재 최대값이 기존 최대값보다 크다면 최대값을 갱신합니다.
            max_val = current_max
        if current_min > min_val:  # 현재 최소값이 기존 최소값보다 크다면 최소값을 갱신합니다.
            min_val = current_min

    return max_val * min_val  # 최대값과 최소값을 곱한 결과를 반환합니다.
