N=int(input())
for i in range(1,2*N):
    print(' '*(min(i,2*N-i)-1)+'*'*(1+2*(N-min(2*N-i,i))))