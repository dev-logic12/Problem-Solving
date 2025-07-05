function solution(order) {
  return order.reduce((acc, cur) => {
    if (cur.includes("ame")) {
      return acc + 4500;
    } else if (cur.includes("latte")) {
      return acc + 5000;
    } else {
      return acc + 4500;
    }
  }, 0);
}