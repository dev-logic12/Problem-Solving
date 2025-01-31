def solution(order):
    # 가격 맵을 만들어서 각 메뉴에 맞는 가격을 설정
    price_map = {
        'latte': 500,  # latte에는 500원 추가
        'basic': 4500,  # 기본 가격 4500원
    }
    
    answer = 0
    for want in order:
        if 'latte' in want:
            answer += price_map['latte'] + price_map['basic']  # latte는 추가금액이 있기 때문에 기본 가격에 더해줌
        else:
            answer += price_map['basic']  # latte가 아니면 기본 가격만 더함
    return answer
