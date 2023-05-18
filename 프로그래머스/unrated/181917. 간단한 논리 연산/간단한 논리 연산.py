def solution(x1, x2, x3, x4):
    return eval(f"({x1} or {x2}) and ({x3} or {x4})")


# def solution(x1, x2, x3, x4):
#     answer = []
#     answer1 = []
#     answer2 = []
#     answer.append(x1)
#     answer.append(x1)
#     answer.append(x3)
#     answer.append(x4)

#     for i in answer:
#         if i == True:
#             answer1.append(i)
#         elif i == False:
#             answer2.append(i)
#     if len(answer1) > len(answer2):
#         return True
#     else:
#         return False
