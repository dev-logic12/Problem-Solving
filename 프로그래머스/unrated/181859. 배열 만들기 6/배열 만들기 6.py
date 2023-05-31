def solution(arr):
    stk = []  # 스택 초기화
    i = 0  # 반복문 인덱스 초기화

    while i < len(arr):
        if len(stk) == 0:
            stk.append(arr[i])
            i += 1
        else:
            if stk[-1] == arr[i]:
                stk.pop()
                i += 1
            elif stk[-1] != arr[i]:
                stk.append(arr[i])
                i += 1
    if len(stk) == 0:
        return [-1]
    return stk
