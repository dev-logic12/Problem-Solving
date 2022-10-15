# import math
    
# def solution(denum1, num1, denum2, num2):
#     x = (num2*denum1) + (num1*denum2)
#     y = num1*num2
#     a = [min(x), y]
#     return a


def solution(denum1, num1, denum2, num2):
    answer = []
    # 두 수가 배수관계일때.
    if max(num1,num2)%min(num1,num2)==0:
        tmp =  max(num1,num2)//min(num1,num2)
        if num1 <=num2:
            answer = [denum1*tmp+denum2, num2]
        else:
            answer = [denum2*tmp+denum1, num1]
    # 두 수가 배수관계가 아닐때.
    else:
        answer = [denum2*num1+denum1*num2, num1*num2]
    
    # 약분되는지 판별
    div = 2
    while min(answer[0],answer[1])>=div:
        if answer[0]%div==0 and answer[1]%div==0:
            answer[0] = answer[0]//div
            answer[1] = answer[1]//div
        else:
            div+=1
    return answer
