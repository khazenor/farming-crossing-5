global.getOrderBookRows = (requestedIds, deliveredIds) => {
  let rows = []
  if (requestedIds.length > 0) {
    rows.push('=== REQUESTED ===')
    rows = Array.prototype.concat(rows, global.generateItemRows(requestedIds))
    rows.push('')
  }
  if (deliveredIds.length > 0) {
    rows.push('=== DELIVERED ===')
    rows = Array.prototype.concat(rows, global.generateItemRows(deliveredIds))
  }
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