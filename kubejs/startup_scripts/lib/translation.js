global.getTransString = (transKey) => {
  return Text.translate(transKey).getString()
}

global.getTranItemName = (itemId) => {
  return global.getTransString(Item.of(itemId).getDescriptionId())
}