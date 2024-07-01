function solution(arr) {
  var answer = [];
  
  // arr의 행(row)과 열(column) 수 계산
  const rowCount = arr.length;
  const colCount = arr[0].length;
  
  // 행(row)과 열(column)의 길이 차이에 따라 처리
  if (rowCount > colCount) {
    // 행이 더 많을 때: 열을 늘려 0으로 채움
    for (let i = 0; i < rowCount; i += 1) {
      const newArr = [...arr[i]];
      for (let j = colCount; j < rowCount; j += 1) {
        newArr.push(0); // 열을 행의 수만큼 0으로 채움
      }
      answer.push(newArr);
    }
  } else if (rowCount < colCount) {
    // 열이 더 많을 때: 부족한 행을 0으로 채운 배열로 추가
    for (let i = 0; i < colCount; i += 1) {
      if (i < rowCount) {
        answer.push(arr[i]);
      } else {
        const newArr = Array(colCount).fill(0); // 새로운 행을 0으로 채움
        answer.push(newArr);
      }
    }
  } else {
    // 행과 열의 길이가 같을 때: 그대로 추가
    answer = arr;
  }
  
  return answer;
}
