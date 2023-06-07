arr = []
num_points = int(input())

for _ in range(num_points):
    arr.append(list(map(int, input().split())))

min_distances = [float('inf')] * (num_points + 1)  # 각 개수(인덱스)마다 최소거리를 저장하기 위해 무한대 값으로 초기화

for i in range(num_points):
    for j in range(num_points):
        x1, y1 = arr[i][0], arr[j][1]  # 모든 점의 좌표를 설정

        distances = []
        for k in range(num_points):  # 한 점에서부터 모든 점까지의 거리를 저장
            x2, y2 = arr[k][0], arr[k][1]
            distances.append(abs(x1 - x2) + abs(y1 - y2))
        distances.sort()  # 최소 거리 순으로 정렬
        sum_ = 0  # 각 거리마다 최소 거리를 저장
        for dist in range(num_points):
            sum_ += distances[dist]  # 각 좌표 개수마다 거리를 더해준다.
            if min_distances[dist + 1] > sum_:  # 현재 거리에 저장된 최소거리보다 지금 구한 거리가 더 최소라면
                min_distances[dist + 1] = sum_  # 그 값을 저장

print(*min_distances[1:])
