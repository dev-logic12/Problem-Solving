r,c = map(int, input().split(' '))
place = []
for _ in range(r):
    arr= list(map(str, input()))
    place.append(arr)

monster_truck =[]
for i in range(r-1):
    for j in range(c-1):
        monster_truck.append([place[i][j],place[i][j+1],place[i+1][j], place[i+1][j+1]])

result =[0 for _ in range(5)]

for i in range(len(monster_truck)):
        if '#' in monster_truck[i] :
            continue
        elif monster_truck[i].count('.') == 4:
            result[0] +=1
        elif monster_truck[i].count('X') == 1:
            result[1] +=1
        elif monster_truck[i].count('X') == 2:
            result[2] +=1
        elif monster_truck[i].count('X') == 3:
            result[3] +=1
        elif monster_truck[i].count('X') == 4:
            result[4] +=1

for i in range(len(result)):
    print(result[i])