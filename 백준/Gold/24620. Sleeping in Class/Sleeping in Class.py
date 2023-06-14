tc = int(input())
for _ in range(tc):
    n = int(input())
    numbers = list(map(int, input().split()))

    _sum = sum(numbers)
    _max = max(numbers)

    prefix = [0]*(n+1)

    for i in range(0, n):
        prefix[i+1] = prefix[i] + numbers[i]

    if _max == min(numbers):
        print(0)
        continue

    answer = n-1
    for d in range(2, n+1)[::-1]:
        if (_sum % d != 0):
            continue
        if (_max > _sum // d):
            continue
        ct = _sum//d
        loc = 0 

        for _ct in range(ct, _sum+1, ct):
            if(_ct not in prefix):
                break
            if (_ct == _sum):
                answer = n-d
        if answer != n-1:
            break 
    print(answer)