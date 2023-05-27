def solution(names):
    answer = []
    answer1 = []
    chunk_size = 5
    for i in range(0, len(names), chunk_size):
        answer.append(names[i:i+chunk_size])        
    for sublist in answer:
        answer1.append(sublist[0])
    return answer1
