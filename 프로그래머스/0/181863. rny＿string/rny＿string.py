import re

def solution(rny_string):
    answer = re.sub("m","rn",rny_string)
    return answer