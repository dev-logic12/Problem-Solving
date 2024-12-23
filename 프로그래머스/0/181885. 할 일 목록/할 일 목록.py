def solution(todo_list, finished):
    do = []
    for i in range(len(finished)):
        if finished[i] == False:
            do.append(todo_list[i])
    return do
