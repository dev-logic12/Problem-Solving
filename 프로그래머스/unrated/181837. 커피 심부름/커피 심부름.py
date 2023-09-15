def solution(order):
    answer = 0
    cheap = ['iceamericano', 'americanoice', 'hotamericano', 'americanohot', 'americano', 'anything']
    expensive = ['icecafelatte', 'cafelatteice', 'hotcafelatte', 'cafelattehot', 'cafelatte']
    
    for menu in order:
        if menu in cheap:
            answer += 4500
        elif menu in expensive:
            answer += 5000
    
    return answer
