global.generateItemRows = (itemIds) => {
  let rows = []
  for (let itemId of itemIds) {
    rows.push(`- ${global.getTranItemName(itemId)}`)
    rows.push(`   (${Item.of(itemId).mod})`)
  }
  return rows
}