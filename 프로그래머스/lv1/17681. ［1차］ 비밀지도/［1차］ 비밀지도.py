def solution(n, arr1, arr2):

    result = []
    for i in range(n):
        result.append(arr1[i] | arr2[i])

    answer = []
    for r in result:
        word = bin(r)[2:]
        word = word.replace("1", "#")
        word = word.replace("0", " ")

        # 앞에 0 붙여주기
        while True:
            if len(word) == n:
                break
            word = " " + word
        answer.append(word)

    return answer