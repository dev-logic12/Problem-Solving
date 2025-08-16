const differences = {
  1: 'w',
  '-1': 's',
  10: 'd',
  '-10': 'a',
};

function solution(numLog) {
  let result = '';
  for (let i = 1; i < numLog.length; i++) {
    result += differences[numLog[i] - numLog[i - 1]];
  }
  return result;
}
