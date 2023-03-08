def solution(angle):
    if angle == 180:
        return 4
    if 90 < angle < 180:
        return 3
    if angle == 90:
        return 2
    if 0<angle < 90:
        return 1 
