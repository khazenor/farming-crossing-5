const ArrayHelper = {
  toStrArray (objArray) {
    let list = []
    for (let val of objArray) {
      list.push(StrHelper.cleanStr(val))
    }
    return list
  },
  toArray(objArray) {
    let list = []
    for (let val of objArray) {
      list.push(val)
    }
    return list
  },
  addToObjectArray (objArray, key, value) {
    if (objArray[key]) {
      objArray[key].push(value)
    } else {
      objArray[key] = [value]
    }
  },
  addToObjectArrayListNoRepeat (objArrayList, key, arrayVal) {
    if (objArrayList[key]) {
      this.pushNewNonEmptyArrayToArrayList(objArrayList[key], arrayVal)
    } else {
      objArrayList[key] = [arrayVal]
    }
  },
  mergeObjectArrays (parentObj, childObj) {
    let workingObj = Object.assign(parentObj)
    for (let childKey in childObj) {
      for (let childValue of childObj[childKey]) {
        this.addToObjectArray(workingObj, childKey, childValue)
      }
    }
    return workingObj
  },
  arrayDiff (parentArray, subtractArray) {
    let arrayDiff = []
    for (let parentVal of parentArray) {
      if (!subtractArray.includes(parentVal)) {
        arrayDiff.push(parentVal)
      }
    }
    return arrayDiff
  },
  pushNonEmptyArraysToArrayList(arrayList, pushArray) {
    if (pushArray.length > 0) {
      arrayList.push(pushArray)
    }
  },
  pushElementIfInProvided(array, element, providedList) {
    if (providedList.includes(element)) {
      array.push(element)
    }
  },
  pushNewNonEmptyArrayToArrayList(arrayList, pushArray) {
    if (!this.arrayListIncludes(arrayList, pushArray)) {
      this.pushNonEmptyArraysToArrayList(
        arrayList,
        pushArray
      )
    }
  },
  arrayListIncludes(arrayList, checkArray) {
    for (let arrayVal of arrayList) {
      if (this.sameArrays(arrayVal, checkArray)) {
        return true
      }
    }
    return false
  },
  sameArrays(array1, array2) {
    if (array1.length !== array2.length) {
      return false
    }
    for (let i = 0; i < array1.length; i++) {
      if (array1[i] !== array2[i]) {
        return false
      }
    }
    return true
  },
  isArray(obj) {
    let stringifyObj = `${obj}`
    return stringifyObj.includes(']') && stringifyObj.includes('[')
  }
  // isArray(obj) {
  //   let stringifyObj = `${obj}`
  //   if (stringifyObj.substring(0, 1) !== '[') {
  //     return false
  //   } else if (stringifyObj.substring(stringifyObj.length - 1) !== ']') {
  //     return false
  //   } else {
  //     return true
  //   }
  // }
}