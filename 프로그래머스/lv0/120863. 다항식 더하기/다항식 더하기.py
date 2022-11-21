def solution(polynomial):
    # 양수만 고려했어도 됨.
    x = polynomial.split(' ')
    x항 = 0
    일반항 = 0
    for i, value in enumerate(x):
        if 'x' in value:
            if len(value) == 1:
                if x[i-1] == '+' or i == 0:
                    x항 += 1
            else:
                if x[i-1] == '+' or i == 0:
                    x항 += int(value[:-1])
        elif value != '+':
            일반항 += int(value)

    if 일반항 == 0 and x항 == 0:
        return f'0'
    elif 일반항 == 0 and x항 != 0:
        if x항 == 1:
            return 'x'
        return f'{x항}x'
    elif 일반항 != 0 and x항 == 0:
        return f'{일반항}'
    elif 일반항 < 0 and x항 > 0:
        if x항 == 1:
            return f'x - {일반항}'
        return f'{x항}x - {일반항}'
    elif 일반항 > 0 and x항 > 0:
        if x항 == 1:
            return f'x + {일반항}'
        return f'{x항}x + {일반항}'
    elif 일반항 > 0 and x항 < 0:
        if x항 == -1:
            return f'-x + {일반항}'
        return f'-{x항}x + {일반항}'
    elif 일반항 < 0 and x항 < 0:
        if x항 == -1:
            return f'-x + {일반항}'
        return f'-{x항}x + {일반항}'