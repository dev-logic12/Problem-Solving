'''
wallpaper = 컴퓨터 바탕화면의 상태, 문자열 배열 
'.' == '#'
최소한의 드래그로 파일 최대한 선택, 삭제 
'''

def solution(wallpaper):
    a, b = [], []
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == '#':
                a.append(i)
                b.append(j)
                
    return [min(a), min(b), max(a)+1, max(b)+1]