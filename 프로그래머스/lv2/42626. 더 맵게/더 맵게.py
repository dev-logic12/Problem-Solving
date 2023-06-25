import heapq

def solution(scoville, k):
    answer = 0 
    heapq.heapify(scoville)
    while len(scoville) > 1:
        min1 = heapq.heappop(scoville)
        if min1 >= k:
            break
        min2 = heapq.heappop(scoville)
        heapq.heappush(scoville, min1+ (min2*2))
        answer += 1 
    else:
        if scoville[0] < k:
            return -1
    return answer 

