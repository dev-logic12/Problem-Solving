from heapq import heappush, heappop 

def solution(k, score):
    answer = []
    heap = []
    for i in score:
        heappush(heap,i)
        if len(heap) > k:
            heappop(heap)
        answer.append(heap[0])
    return answer 