'''
긴거 빅에 넣고
짧은거 스몰에 넣고 
각 맥스를 곱하기 
'''

def solution(sizes):
    answer = 0
    big = []
    small = []
    for i in range(len(sizes)):
        if sizes[i][0] >= sizes[i][1]:
            big.append(sizes[i][0])
            small.append(sizes[i][1])
        else:
            big.append(sizes[i][1])
            small.append(sizes[i][0])
    answer = max(big) * max(small)
    return answer