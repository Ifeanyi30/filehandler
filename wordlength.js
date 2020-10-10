function findLongestWordLength(str) {
  var list = str.split(" ")
  var numList = [];
  for (let item in list){
    numList.push(item.length);
  }
  return Math.max(...numList);
}

findLongestWordLength("The quick brown fox jumped over the lazy dog");