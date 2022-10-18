# def solution(num_list):
#     a = int(num_list)
#     answer = [len(a % 2 ==0),len(a % 2 !=0)]
#     return answer


def solution(num_list):
    even = list(filter(lambda x: x % 2==0, num_list))
    return (len(even), len(num_list)-len(even))




# def solution(num_list):
#     answer = [0,0]
#     for n in num_list:
#         answer[n%2]+=1
#     return answer

# def solution(num_list):
#     even = list(filter(lambda x: x%2==0, num_list))
#     return [len(even), len(num_list)-len(even)]

# def solution(num_list):
#     even = list(filter(lamda x: x%2==0, num_list))
#     return [len(even), len(num_list)-len(even)]
