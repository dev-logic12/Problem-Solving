def solution(arr, flag):
    vector = []
    
    for i in range(len(flag)):
        if flag[i]:
            for j in range(arr[i] * 2):
                vector.append(arr[i])
        else:
            z = 0
            num = len(vector) - 1
            while z < arr[i]:
                vector.pop(num)
                num -= 1
                z += 1
    
    answer = vector
    return answer



