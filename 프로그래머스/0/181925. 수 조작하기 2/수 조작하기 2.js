function solution(numLog) {
  const convert = {
    1: 'w',
    '-1': 's',
    10: 'd',
    '-10': 'a',
  };

  return numLog
    .map((v, i, arr) => (i === 0 ? '' : convert[v - arr[i - 1]]))
    .join('');
}
