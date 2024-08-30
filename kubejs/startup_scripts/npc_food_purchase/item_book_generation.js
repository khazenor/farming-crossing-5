global.getOrderBookRows = (requestedIds, deliveredIds) => {
  let rows = []
  rows.push('=== REQUESTED ===')
  rows = Array.prototype.concat(rows, global.generateItemRows(requestedIds))
  rows.push('')
  rows.push('=== DELIVERED ===')
  rows = Array.prototype.concat(rows, global.generateItemRows(deliveredIds))
  return rows
}

global.generateItemRows = (itemIds) => {
  let rows = []
  for (let itemId of itemIds) {
    rows.push(`- ${global.getTranItemName(itemId)}`)
    rows.push(`   (${Item.of(itemId).mod})`)
  }
  return rows
}