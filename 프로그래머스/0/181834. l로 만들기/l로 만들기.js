const solution = myString => 
  myString.split('').map(char => (char >= 'a' && char <= 'k' ? 'l' : char)).join('');
