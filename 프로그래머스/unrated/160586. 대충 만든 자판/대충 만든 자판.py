'''
존재하지 않으면 -1을 리턴 

'''

def solution(keymap, targets):
    answer = []
    for target in targets:
        count, isTrue = 0, True
        for key in target:
            min_index = min([101] + [k.find(key)+1 for k in keymap if k.find(key)+1 != 0])
            if min_index == 101:
                isTrue = False
                break
            count += min_index
        answer.append(count if isTrue else -1)

    return answer