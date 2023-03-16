'''
조합으로 푸는 문제 
4가지 단어를 조합해서 가능한 갯수를 리턴 
'''
def solution(babbling):
    answer = 0
    for i in babbling:
        for j in ['aya','ye','woo','ma']:
            if j*2 not in i:
                i=i.replace(j,' ')
                print("i =", i)
        if len(i.strip())==0:
            answer +=1
    return answer