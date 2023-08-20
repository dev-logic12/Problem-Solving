def solution(n, times):
    max_ = min(times)*n
    min_ = 1
    while min_+1 != max_:
        search = (max_+min_)//2
        done = sum([search//t for t in times])
        if done >= n:
            max_ = search
        else:
            min_ = search
    return max_    