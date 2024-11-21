def solution(myString):
    result = ''
    for char in myString:
        if char == 'a':
            result += 'A'
        elif char == 'A':
            result += 'A'
        elif char.isupper():
            result += char.lower()
        else:
            result += char
    return result
