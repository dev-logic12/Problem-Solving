from collections import Counter

def solution(array):
    # 배열의 빈도수를 계산하여 딕셔너리 형태로 저장
    count_dict = Counter(array)
    
    # 빈도수가 가장 큰 값을 찾음
    max_count = max(count_dict.values())
    
    # 빈도수가 가장 큰 값들을 모두 찾음
    modes = [num for num, count in count_dict.items() if count == max_count]
    
    # 최빈값이 하나 이상인 경우 -1 반환, 아니면 최빈값 반환
    if len(modes) > 1:
        return -1
    else:
        return modes[0]
