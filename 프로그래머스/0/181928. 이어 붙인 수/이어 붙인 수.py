def solution(num_list):
    h = []
    z = []
    for i in num_list:
        if i % 2 != 0:
            h.append(str(i))
        else:
            z.append(str(i))
    return int(''.join(h))+int(''.join(z))