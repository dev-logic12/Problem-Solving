e,s,m,cnt = 1,1,1,1

n_e, n_s, n_m = map(int, input().split())

while True:
    if n_e==e and n_s==s and n_m==m:
        break
    e+=1 ; s+= 1; m+=1; cnt+=1
    if e>=16 : e-=15
    if s>=29 : s-=28
    if m>=20 : m-=19

print(cnt)