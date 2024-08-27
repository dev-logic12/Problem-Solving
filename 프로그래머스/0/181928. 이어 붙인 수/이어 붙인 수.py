def solution(num_list):
    odd_numbers = []
    even_numbers = []
    
    for i in num_list:
        if i % 2 != 0:
            odd_numbers.append(str(i))
        else:
            even_numbers.append(str(i))
    
    return int(''.join(odd_numbers)) + int(''.join(even_numbers))
