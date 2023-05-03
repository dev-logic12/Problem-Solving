def solution(rny_string):
    answer = ''
    for i in rny_string:
        answer = rny_string.replace('m', 'rn')    
    return answer


# rny_string	= "masterpiece"	
# print(solution(rny_string))