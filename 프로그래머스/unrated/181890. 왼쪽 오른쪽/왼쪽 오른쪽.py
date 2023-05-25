def solution(str_list):
    answer = next((i for i, s in enumerate(str_list) if s == "l" or s == "r"), -1)

    if answer == -1:
        return []
    elif str_list[answer] == "l":
        return str_list[:answer]
    else:
        return str_list[answer + 1:]
