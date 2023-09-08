def solution(arr):
    return  [arr[i] for i in range(len(arr)) if not(arr[i:i+1] == arr[i+1:i+2])]