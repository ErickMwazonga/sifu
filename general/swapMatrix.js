// Given an square matrix, turn it by 90 degrees in clockwise direction.
// Given an square matrix, turn it by 90 degrees in anti-clockwise direction.

// Input:
//  [[1, 2, 3],
//   [4, 5, 6],
//   [7, 8, 9]]

// Output - Clockwise:
//  [[1, 2, 3],
//   [4, 5, 6],
//   [7, 8, 9]]

// Output - AntiClockwise:
//  [[3, 6, 9],
//   [2, 5, 8],
//   [1, 4, 7]]


const transponseMatrix = matrix => {
    const matrixLength = matrix.length;
    let tempMatrix = []

    if(matrixLength === 0) return []

    for(let i = 0; i < matrixLength; i++) {
        tempMatrix[i] = [];

        for(let j = 0; j < matrixLength; j++) {
            tempMatrix[i].push(matrix[j][i])
        }
    }

    return tempMatrix;
}

const swapMatrixClockwise = matrix => {
    const matrixLength = matrix.length;
    let tempMatrix = []

    if(matrixLength === 0) return []

    for(let i = 0; i < matrixLength; i++) {
        tempMatrix[i] = [];

        for(let j = 0; j < matrixLength; j++) {
            tempMatrix[i].unshift(matrix[j][i])
        }
    }

    return tempMatrix;
}

const transposeClockwise = matrix => {
    const transposed = transponseMatrix(matrix);
    const temp = transposed.map(row => row.reverse());

    return temp;
}

const transposeAntiClockwise = matrix => {
    const transposed = transponseMatrix(matrix);
    return transposed.reverse();
}

const a = [[1,2,3], [4,5,6], [7,8,9]];

console.log(transponseMatrix(a));
console.log(transposeClockwise(a));
console.log(transposeAntiClockwise(a));

// Expected: '[[3, 6, 9, 12], [2, 5, 8, 11], [1, 4, 7, 10]]', instead got: '[[undefined, undefined, undefined, undefined], [3, 6, 9, 12], [2, 5, 8, 11], [1, 4, 7, 10]]'
// Expected: '[[10, 7, 4, 1], [11, 8, 5, 2], [12, 9, 6, 3]]', instead got: '[[10, 7, 4, 1], [11, 8, 5, 2], [12, 9, 6, 3], [undefined, undefined, undefined, undefined]]'
// Expected: '[[3], [2], [1]]', instead got: '[[1]]'
// Expected: '[[1], [2], [3]]', instead got: '[[1]]'
// Expected: '[[3, 2, 1]]', instead got: '[[1]]'