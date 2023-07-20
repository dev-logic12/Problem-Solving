import heapq

def solution(scoville, k):
    heapq.heapify(scoville) 
    answer = 0
    
    while scoville[0] < k:
        if len(scoville) <= 1:
            return -1
        min1 = heapq.heappop(scoville)
        min2 = heapq.heappop(scoville)
        heapq.heappush(scoville, min1 + (min2 * 2))
        answer += 1 
    
    return answer
