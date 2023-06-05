def solution(order):
    answer = 0
    a = ['iceamericano', 'americanoice', 'hotamericano', 'americanohot', 'americano', 'anything']
    l = ['icecafelatte', 'cafelatteice', 'hotcafelatte', 'cafelattehot', 'cafelatte']
    
    for menu in order:
        if menu in a:
            answer += 4500
        elif menu in l:
            answer += 5000
    
    return answer
