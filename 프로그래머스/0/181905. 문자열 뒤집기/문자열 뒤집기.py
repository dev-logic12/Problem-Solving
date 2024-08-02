def solution(my_string, s, e):
    # 부분 문자열들을 변수에 저장
    prefix = my_string[:s]
    substring_to_reverse = my_string[s:e+1]
    suffix = my_string[e+1:]
    
    # 각 부분 문자열들을 조합하여 결과 반환
    return prefix + substring_to_reverse[::-1] + suffix
