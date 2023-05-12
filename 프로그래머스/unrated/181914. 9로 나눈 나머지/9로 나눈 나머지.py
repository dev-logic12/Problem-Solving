def solution(number):
    answer = 0
    for i in number:
        answer += int(i) 
    answer1 = answer % 9
    return answer1
number = "78720646226947352489"	
print(solution(number))