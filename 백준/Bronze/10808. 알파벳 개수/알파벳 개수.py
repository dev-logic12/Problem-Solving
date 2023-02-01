s = input()
al = "abcdefghijklmnopqrstuvwxyz"
for i in range(26):
    x = al[i]
    sx = s.count(x)
    print(sx, end=" ")