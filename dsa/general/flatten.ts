/*
Flatten an Array?
https://johnkavanagh.co.uk/articles/flattening-arrays-in-javascript/

const nestedArray = [1, [2, [3, [4, 5]]], 6]
const flatArray = [1, 2, 3, 4, 5, 6]
*/

// Using built-in flat method
const flattenV1 = (arr: any[], depth: number = Infinity): any[] => arr.flat(depth)

// Using recursion
const flattenV2 = (arr: any[]): any[] => {
  const result: any[] = []

  for (const item of arr) {
    if (Array.isArray(item)) {
      result.push(...flattenV2(item))
    } else {
      result.push(item)
    }
  }

  return result
}

// Using reduce
const flattenV3 = (arr: any[]): any[] => (
  arr.reduce((acc, val) =>
    Array.isArray(val) ? acc.concat(flattenV3(val)) : acc.concat(val), []
  )
)

// Using stack
const flattenV4 = (arr: any[]): any[] => {
  const stack = [...arr]
  const result: any[] = []

  while (stack.length) {
    const next = stack.pop()
    if (Array.isArray(next)) {
      stack.push(...next)
    } else {
      result.push(next)
    }
  }
  return result.reverse()
}
