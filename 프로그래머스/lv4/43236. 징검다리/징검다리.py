def solution(distance, rocks, n):
    if len(rocks) == n:
        return distance

    rocks.sort()
    rocks.append(distance)
    answer = 0
    start, end = 0, distance

    while start <= end:
        mid = (start + end) // 2
        prev_rock = 0
        removed_rocks = 0

        for rock in rocks:
            if rock - prev_rock < mid:
                removed_rocks += 1
            else:
                prev_rock = rock

        if removed_rocks > n:
            end = mid - 1
        else:
            answer = mid
            start = mid + 1

    return answer
