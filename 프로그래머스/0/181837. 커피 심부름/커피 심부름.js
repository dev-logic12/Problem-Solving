function solution(order) {
  const prices = {
    americano: 4500,
    latte: 5000
  };

  return order.reduce((total, item) => {
    return total + (item.includes("latte") ? prices.latte : prices.americano);
  }, 0);
}
