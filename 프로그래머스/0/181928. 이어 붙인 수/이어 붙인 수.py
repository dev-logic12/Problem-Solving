def solution(num_list):
    answer = 0
    hol=""
    zzak=""
    for i in num_list:
        if i%2!=0:
            hol+=str(i)
        else:
            zzak+=str(i)
    return int(hol)+int(zzak)