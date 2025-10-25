function solution(num_list) {
    const len = num_list.length;
    const a = num_list[len - 1];  
    const b = num_list[len - 2];  
    return [...num_list, a > b ? a - b : a * 2];
}
