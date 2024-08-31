global.getTransString = (transKey) => {
  return Text.translate(transKey).getString()
}

global.getTranItemName = (itemId) => {
  return global.getTransString(Item.of(itemId).getDescriptionId())
}

global.getFormattedTran = (transKey, insertStrs) => {
  let parentStr = global.getTransString(transKey)
  for (let i = 0; i<insertStrs.length; i++) {
    let replaceStr = `%${i+1}`
    parentStr = parentStr.replace(replaceStr, `${insertStrs[i]}`)
  }
  return parentStr
}
