n = int(input())
#기다리는 사람들을 리스트의 형태로 입력 받음 
people = list(map(int, input().split()))
#정답 변수의 값을 0으로 초기화 진행 
num = 0
#최솟값 도출을 위해 작은 순서대로(오름차순)으로 정렬 
people.sort()

for i in range(1, n+1):
    num += sum(people[0:i])  
print(num)