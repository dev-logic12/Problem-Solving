import heapq

def solution(scoville, k):
    answer = 0
    heapq.heapify(scoville)  # scoville 리스트를 힙으로 변환
    while len(scoville) > 1:  # 음식이 2개 이상 남아있는 동안 반복
        min1 = heapq.heappop(scoville)  # 가장 작은 원소를 pop
        if min1 >= k:  # 가장 작은 원소가 k보다 크거나 같으면 반복 종료
            break
        min2 = heapq.heappop(scoville)  # 두 번째로 작은 원소를 pop
        heapq.heappush(scoville, min1 + (min2 * 2))  # 두 개의 원소를 섞어서 다시 push
        answer += 1  # 섞은 횟수를 카운트
    else:  # 반복이 정상적으로 종료된 경우 (k보다 크거나 같은 원소가 없는 경우)
        if scoville[0] < k:  # 남은 가장 작은 원소가 k보다 작으면 -1 반환
            return -1
    return answer
