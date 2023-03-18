


from collections import Counter

def solution(participant, completion):
    participant_counts = Counter(participant)
    completion_counts = Counter(completion)
    return list((participant_counts - completion_counts).keys())[0]