function SnailSortRecursive(array) { 
  var result = [];

  if (array.length == 0 )
    return result;

  var max = array[0].length -1;

  //grab the first row | result.push.apply(result,array[0])
  for (var i=0;i<=max;i++){
    result.push(array[0][i]);
  }

  //grab the last column
  for (var i=1;i< max;i++){
    result.push(array[i][max]);
  }

  //grab the last row
  for (var i=max;i>=0;i--){
    result.push(array[max][i]);
  }

  //grab the first column
  for (var  i=max-1;i> 0;i--){
    result.push(array[i][0]);
  } 

  subarray = [];
  //form the inner matrix
  for (var i=1;i<max;i++)
  {
    subarray.push(array[i].splice(1,max-1));
  }

  //call it recursively
  result = result.concat( SnailSortRecursive(subarray));

  return result;
}

input = [[1,2,3],[4,5,6],[7,8,9]]
input2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
SnailSortRecursive(input2); 