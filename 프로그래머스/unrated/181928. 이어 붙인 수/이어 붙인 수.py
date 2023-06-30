def solution(num_list):
    even = ""
    odd = ""
    for num in num_list:
        if num % 2 == 0:
            even += str(num)
        else:
            odd += str(num)
    even_sum = int(even) if even else 0
    odd_sum = int(odd) if odd else 0
    return int(odd) + int(even)
