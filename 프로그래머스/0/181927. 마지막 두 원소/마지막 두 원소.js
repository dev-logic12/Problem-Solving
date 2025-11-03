function solution(num_list) {
  const l = num_list.length;
  return [...num_list, num_list[l - 1] > num_list[l - 2] 
    ? num_list[l - 1] - num_list[l - 2] 
    : num_list[l - 1] * 2];
}
