def solution(rank, attendance):
    answer = 0
    rank_index = [[rank[i], i] for i in range(len(rank))]
    rank_index.sort(key=lambda x: x[0])
    result = []
    
    for i in range(len(attendance)):
        if attendance[rank_index[i][1]]:
            result.append(rank_index[i][1])
        if len(result) == 3:
            break
    
    first = result[0] * 10000
    second = result[1] * 100
    third = result[2]
    answer = first + second + third
    
    return answer

