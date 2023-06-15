def recur(idx, guitar, song):
    global maxi_song, mini_guitar

    if song > maxi_song:
        maxi_song = song
        mini_guitar = guitar
    elif song == maxi_song:
        mini_guitar = min(guitar, mini_guitar)

    if idx == n:
        return

    for j in range(m):
        if dict[idx][j] == "Y":
            playlist[j] += 1

    recur(idx + 1, guitar + 1, sum(l != 0 for l in playlist))

    for k in range(m):
        if dict[idx][k] == "Y":
            playlist[k] -= 1

    recur(idx + 1, guitar, song)


n, m = map(int, input().split())

dict = {}

for i in range(n):
    guitar, songs = map(str, input().split())
    dict[i] = list(map(str, songs.rstrip("")))

playlist = [0] * m
maxi_song = 0
mini_guitar = float('inf')

recur(0, 0, 0)

if maxi_song:
    print(mini_guitar)
else:
    print(-1)
