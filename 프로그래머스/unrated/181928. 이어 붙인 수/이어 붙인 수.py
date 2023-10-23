def solution(num_list):
    hol = []
    zzak = []
    for i in num_list:
        if i % 2 != 0:
            hol.append(str(i))
        else:
            zzak.append(str(i))
    return int(''.join(hol)) + int(''.join(zzak))


