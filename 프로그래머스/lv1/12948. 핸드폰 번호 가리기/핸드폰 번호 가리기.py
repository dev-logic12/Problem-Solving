def solution(phone_number):
    # answer = phone_number.replace(phone_number[:-5], '*')
    answer = "*"*(len(phone_number)-4)
    return answer + (phone_number[-4:])