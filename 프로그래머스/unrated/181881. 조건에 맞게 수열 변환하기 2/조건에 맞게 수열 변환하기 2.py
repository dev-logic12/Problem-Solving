def solution(arr):
    idx = 0
    prev_arr = arr
    
    while True:
        # 현재 배열을 조건에 맞게 변환
        change_cur_arr = [a//2 if a >= 50 and a % 2 == 0 else a*2+1 if a < 50 and a % 2 == 1 else a for a in prev_arr]
        
        # 이전의 모든 배열과 현재 모든 배열의 요소 비교
        is_all_same = all(a == b for a, b in zip(prev_arr, change_cur_arr))
        
        if is_all_same:
            break
        
        idx += 1
        
        # 현재 배열을 이전 배열 변수에 저장함
        prev_arr = change_cur_arr
    
    return idx
