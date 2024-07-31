def solution(todo_list, finished):
    todo = []
    for i in range(len(finished)):
        if finished[i] == False:
            todo.append(todo_list[i])
    return todo
