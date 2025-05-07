const ObjectHelper = {
  strifyKeys (obj) {
    let newObj = {}
    for (let key in obj) {
      newObj[`${key}`] = obj[key]
    }
    return newObj
  },
  getNestedValue (object, keysString) {
    let keys = keysString.split('/')
    let curObj = object
    for (let key of keys) {
      if (typeof curObj !== 'object') {
        return null
      } else if (key in curObj) {
        curObj = curObj[key]
      } else {
        return null
      }
    }
    return curObj
  }
}