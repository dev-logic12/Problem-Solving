def solution(arr):
    flat = [arr[i][j] for i in range(len(arr)) for j in range(i)]
    return int(flat == [arr[j][i] for i in range(len(arr)) for j in range(i)])
