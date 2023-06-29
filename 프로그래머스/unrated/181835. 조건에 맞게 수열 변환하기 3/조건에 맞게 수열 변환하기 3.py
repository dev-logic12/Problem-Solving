def solution(arr, k):
    answer = []
    for i in range(len(arr)):
        if k%2 != 0:
            arr[i] *= k
            answer.append(arr[i])
        else:
            arr[i] += k
            answer.append(arr[i])
    return answer