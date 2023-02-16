def solution(partcipant, completion):
    partcipant.sort()
    completion.sort()

    for i in range(len(completion)):
        if partcipant[i] != completion[i]:
            return partcipant[i]
    return partcipant[-1]