def solution(num_list):
    answer = 0
    hol = ''
    even = ''
    for i in num_list:
        if i %2 != 0:
            hol += str(i) 
        else:
            even += str(i)
    
    return int(hol) + int(even)