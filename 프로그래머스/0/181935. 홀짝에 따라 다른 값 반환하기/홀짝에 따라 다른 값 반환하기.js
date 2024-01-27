function solution(n) {
    if (n % 2 === 1) {  
        return Array.from({ length: Math.ceil(n / 2) }, (_, index) => 2 * index + 1)
            .reduce((sum, num) => sum + num, 0);  
    } else {  
        return Array.from({ length: Math.ceil(n / 2) }, (_, index) => 2 * (index + 1))
            .reduce((sum, num) => sum + num ** 2, 0);  
    }
}
