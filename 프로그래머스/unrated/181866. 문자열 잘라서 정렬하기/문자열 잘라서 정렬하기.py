def solution(myString):
    split_strings = myString.split('x')
    answer = sorted(string for string in split_strings if string != '')
    return answer
