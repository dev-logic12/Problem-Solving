def solution(arr, queries):
    answer = []
    for query in queries:
        s, e, k = query
        tmp = sorted(filter(lambda x: s <= arr.index(x) <= e and x > k, arr))
        answer.append(tmp[0] if tmp else -1)
    return answer
