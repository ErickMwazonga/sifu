function longestPalindrome(str) {
  const _str = str.toString().toLowerCase().replace(/[^0-9a-zA-Z]/g, '');
    
  const res = {};
  _str.split("").forEach((el, idx) => res[el] = res[el] ? res[el] + 1 : 1)

  if (_str.length === 1) {
    return 1;
  }

  let total = 0;
  for (let [k, v] of Object.entries(res)) {
    if(res[k] % 2 != 0) {
      res[k] -= 1;
    }
    
    total += res[k];
  }
  

  return total > 1 ? total + 1 : 1;
}
