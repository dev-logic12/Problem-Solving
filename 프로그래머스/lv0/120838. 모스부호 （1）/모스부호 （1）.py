def solution(letter):
    morse = { 
        '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
        '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
        '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
        '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
        '-.--':'y','--..':'z'
    }
    
    # 입력 문자열을 공백 문자를 기준으로 나누어 리스트로 저장합니다.
    words = letter.split()
    
    # 각각의 문자열을 모스 부호에서 알파벳 문자로 변환합니다.
    decoded_words = []
    for word in words:
        decoded_word = ''
        for code in word.split():
            decoded_word += morse[code]
        decoded_words.append(decoded_word)
    
    # 변환된 알파벳 문자열을 하나의 문자열로 합쳐서 반환합니다.
    return ''.join(decoded_words)