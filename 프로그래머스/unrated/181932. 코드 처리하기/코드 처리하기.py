def solution(code):
    mode = 0
    ret = []
    for idx in range(len(code)):
        if mode == 0:
            if code[idx] != '1':
                if idx % 2 == 0:
                    ret.append(code[idx])
            elif code[idx] == '1':
                mode = 1
        elif mode == 1:
            if code[idx] != '1':
                if idx % 2 != 0:
                    ret.append(code[idx])
            elif code[idx] == '1':
                mode = 0

    if not ret:
        return 'EMPTY'
    return ''.join(ret)


# code = "abc1abc1abc"	
# print(solution(code))

# code = "abc1abc1abc"	
# print(solution(code))