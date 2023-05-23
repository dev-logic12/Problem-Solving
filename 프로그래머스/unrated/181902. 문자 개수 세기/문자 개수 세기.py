def solution(my_string):
    counts = [0] * 52  # 알파벳 개수를 저장할 배열 초기화

    for char in my_string:
        if 'A' <= char <= 'Z':
            counts[ord(char) - ord('A')] += 1
        elif 'a' <= char <= 'z':
            counts[ord(char) - ord('a') + 26] += 1

    return counts
