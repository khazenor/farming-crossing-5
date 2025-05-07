const ArrayLib = {
  repeatArr (value, length) {
    let arr = []
    for (let i = 0; i < length; i++) {
      arr.push(value)
    }
    return arr
  }
}