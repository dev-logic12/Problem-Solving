def solution(num_list):
    answer = next((i for i, x in enumerate(num_list) if x < 0), -1)
    return answer