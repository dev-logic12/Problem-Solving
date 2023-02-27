from collections import Counter  

def solution(participant, completion):
    return list((Counter(participant)- Counter(completion)).keys())[0]




# list((Counter(participant) - Counter(completion)).keys())[0]