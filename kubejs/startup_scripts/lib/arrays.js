global.getRandomSubArray = (parentArr, numToPick) => {
  let subArray = []
  for (let i = 0; i<numToPick; i++) {
    let randomVal = global.getRandomArrayElement(parentArr)
    while (subArray.includes(randomVal)) {
      randomVal = global.getRandomArrayElement(parentArr)
    }
    subArray.push(randomVal)
  }
  return subArray
}

global.getRandomArrayElement = (arr) => {
  return arr[Math.floor(Math.random()*arr.length)]
}

global.getObjArrIncludes = (objArr, checkValue) => {
  for (let value of objArr) {
    value = global.genStrFromObj(value)
    if (`${value}` === checkValue) {
      return true
    }
  }
  return false
}