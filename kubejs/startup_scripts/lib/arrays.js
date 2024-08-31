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

global.arrFromObj = (objArr) => {
  let newArray = []
  for (let value of objArr) {
    value = global.genStrFromObj(value)
    newArray.push(value)
  }
  return newArray
}

global.getObjArrIncludes = (objArr, checkValue) => {
  return global.arrFromObj(objArr).includes(checkValue)
}