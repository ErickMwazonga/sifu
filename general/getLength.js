// let res = [];

// const getLength = arr => {
//     arr.forEach(el => {
//         Array.isArray(el) ? getLength(el) : res.push(el);
//     });

//     return res.length;
// }

function getLength(arr) {
	let res = [];
	
	function temp(arr) {
		arr.forEach(el => {
			Array.isArray(el) ? temp(el) : res.push(el);
        });
        return res;
	}

	return temp(arr).length;
}


// getLength([1, [2, 3]]) ➞ 3
// getLength([1, [2, [3, 4]]]) ➞ 4
// getLength([1, [2, [3, [4, [5, 6]]]]]) ➞ 6
// getLength([1, [2], 1, [2], 1]) ➞ 5

// console.log(getLength([1, [2, 3]]))
// console.log(getLength([1, [2, [3, 4]]]))
// console.log(getLength([1, [2, [3, [4, [5, 6]]]]]))
console.log(getLength([1, [2], 1, [2], 1]))