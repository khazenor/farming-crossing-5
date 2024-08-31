global.randomArrayElement = (arr) => {
  console.log('testing hello')
  return arr[Math.floor(Math.random()*arr.length)]
}

global.randomSubArray = (parentArr, numToPick) => {
  let subArray = []
  for (let i = 0; i<numToPick; i++) {
    let randomVal = global.randomArrayElement(parentArr)
    while (subArray.includes(randomVal)) {
      randomVal = global.randomArrayElement(parentArr)
    }
    subArray.push(randomVal)
  }
  return subArray
}