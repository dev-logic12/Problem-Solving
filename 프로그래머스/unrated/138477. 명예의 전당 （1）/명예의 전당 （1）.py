'''
힙 자료구조 활용 
첫날-마지막날 점수를 차례로 힙에 추가 
힙의 원소의 개수가 k보다 크면 현재 힙에서 점수가 가장낮은 원소의 값 제거 
'''

from heapq import heappop, heappush

def solution(k, score):
    answer = []
    heap = []
    for s in score:
        heappush(heap, s)
        if len(heap) > k:
            heappop(heap)
        answer.append(heap[0])
    return answer 



'''
점수 리스트에서
'''
# def solution(k, score):
#     answer = []
#     answer1 = []
    
#     for score in score:
#         answer1.append(score)
#         answer1 = sorted(answer1, reverse=True)[:k]
        
#         answer.append(min(answer1))
        
#     return answer
    