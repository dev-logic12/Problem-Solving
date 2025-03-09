function solution(num_list) {
    let even = 0, odd = 0;

    num_list.forEach((v, idx) => {
        if (idx % 2 === 0) even += v;
        else odd += v;
    });

    return Math.max(even, odd); 
}
