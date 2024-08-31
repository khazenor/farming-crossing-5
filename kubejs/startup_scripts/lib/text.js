global.genStrFromPlayerObj = (obj) => {
  return global.replaceAll(`${obj}`, '"', '')
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
  return str
}