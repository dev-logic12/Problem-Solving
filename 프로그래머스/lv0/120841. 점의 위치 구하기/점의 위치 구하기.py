def solution(dot):
    answer = 0
    for i in dot:
        if dot[0] > 0 and dot[1] >0:
            return 1
        if dot[0] >0 and dot[1] <0:
            return 4
        if dot[0] <0 and dot[1] >0:
            return 2 
        if dot[0] <0 and dot[1] <0:
            return 3
