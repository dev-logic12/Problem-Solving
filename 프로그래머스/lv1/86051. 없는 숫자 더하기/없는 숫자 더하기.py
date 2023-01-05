def solution(numbers):
    #없는 수를 찾아서
    #더한다 
    num = [1,2,3,4,5,6,7,8,9]
    answer = list(set(num)- set(numbers))
    return sum(answer)