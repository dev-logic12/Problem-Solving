def solution(answers):
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]
    c1, c2, c3 = 0, 0, 0
    cnt = []
    answer = []
    for i in range(len(answers)):
        s1 = i%5
        s2 = i%8
        s3 = i%10 

        if answers[i] == a[s1]:
            c1 += 1
        if answers[i] == b[s2]:
            c2 += 1 
        if answers[i] == c[s3]:
            c3 += 1 
    answer = max(c1, c2, c3)

    if answer == c1:
        cnt.append(1)
    if answer == c2: 
        cnt.append(2)
    if answer == c3: 
        cnt.append(3)
    return cnt 