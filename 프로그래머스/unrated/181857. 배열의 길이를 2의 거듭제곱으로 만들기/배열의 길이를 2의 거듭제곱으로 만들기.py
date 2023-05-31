def solution(arr):
    pow2 = [0, 2, 4, 8, 16, 32, 64, 128, 256, 512]
    arr_len = len(arr)
    idx = 0
    for i in range(len(pow2)):
        if arr_len < pow2[i]:
            break
        idx = pow2[i]
    
    zero_arr = [0] * idx
    
    return arr + zero_arr[:idx-arr_len]
