def recur(numbers, sum, target):
    if numbers == []:
        if sum == target:
            return 1
        else:
            return 0
    return recur(numbers[1:], sum + numbers[0], target) + recur(numbers[1:], sum - numbers[0], target)

def solution(numbers, target):
    return recur(numbers, 0, target)