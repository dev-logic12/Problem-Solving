n, k = map(int, input().split())

# 1부터 n까지의 사람들을 리스트로 만듦
people = list(range(1, n+1))

# 제거된 사람들을 저장할 리스트
result = []

# k번째 사람을 제거해나가는 과정
# 제거된 사람들은 result에 저장
index = k-1
while people:
    index = index % len(people)
    result.append(str(people.pop(index)))
    index += k-1

# 요세푸스 순열 출력
print("<" + ", ".join(result) + ">")
