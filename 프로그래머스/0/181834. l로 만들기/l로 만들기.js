function solution(myString) {
    return [...myString].map(char => char >= 'a' && char <= 'l' ? 'l' : char).join('');
}
