def solution(array, commands):
    answer = []
    for i in commands:
        i, j, k = i 
        array1 = array[i-1:j]
        array1.sort()
        answer.append(array1[k-1])
    return answer

