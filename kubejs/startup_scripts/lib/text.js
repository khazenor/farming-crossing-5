global.genStrFromObj = (obj) => {
  return global.cleanString(`${obj}`)
}

global.genNumFromObj = (obj) => {
  return parseFloat(`${obj}`.replace('d', ''))
}

global.replaceAll = (parentStr, pattern, replace) => {
  while (parentStr.includes(pattern)) {
    parentStr = parentStr.replace(pattern, replace)
  }
  return parentStr
}

global.cleanString = (str) => {
  str = global.replaceAll(str, '"','')
  str = global.replaceAll(str, "'", '')
  str = global.replaceAll(str, '[','')
  str = global.replaceAll(str, ']','')
  return str
}