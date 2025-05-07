const StrHelper = {
  cleanFloor: (number) => {
    let decimal = '.'
    let stringVal = `${number}`
    if (stringVal.includes(decimal)) {
      return stringVal.split(decimal)[0]
    } else {
      return stringVal
    }
  },
  replaceAll (parentStr, findStr, replaceStr) {
    let replacedStr = ''
    let findLen = findStr.length
    for (let i = 0; i < parentStr.length; i++) {
      if (i < parentStr.length - findLen) {
        let workingStr = parentStr.substring(i, i + findLen)
        if (workingStr === findStr) {
          replacedStr = replacedStr + replaceStr
          continue
        }
      }
      replacedStr = replacedStr + parentStr.substring(i, i + 1)
    }
    return replacedStr
  },
  cleanStr (str) {
    let cleanedStr = `${str}`
    cleanedStr = cleanedStr.replace('literal{', '')
    cleanedStr = cleanedStr.replace('}', '')
    cleanedStr = this.replaceAll(cleanedStr, '"', '')
    return cleanedStr
  },
  objToMinecraftStr(obj) {
    return JSON.stringify(obj)
  },
  isStr(obj) {
    let stringifyObj = `${obj}`
    let badIds = ['{', '}', '[', ']', ',']
    for (let badId of badIds) {
      if (stringifyObj.includes(badId)) {
        return false
      }
    }
    return true
  },
  isStrRobust(ingObj) {
    if (typeof ingObj === 'string') {
      return true
    }
    if (typeof ingObj === 'object') {
      if (!this.isStr(ingObj)) {
        return false
      }
      let ingArray = ArrayHelper.toArray(ingObj)
      return (
        ingArray[0] &&
        ingArray[0].length === 1 &&
        typeof ingArray[0] === 'string'
      )
    }
  }
}