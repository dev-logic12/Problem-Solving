def solution(my_string, overwrite_string, s):
    return my_string[:s]+overwrite_string+ my_string[s+len(overwrite_string):]
    # answer1 = my_string[:s]
    # answer = my_string[s:len(overwrite_string)]
    # answer2 = my_string.replace(answer1, overwrite_string)
    # answer3 = my_string[len(answer1)+len(answer)+1:]
    # return answer1