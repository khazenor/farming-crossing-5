ItemEvents.entityInteracted(event => {
  let handItemId = event.player.mainHandItem.id
  if (global.isItemAMenu(handItemId)) {
    let order = global.getOrderObject(
      event.target,
      handItemId
    )
    event.player.persistentData.activeOrder = order
    let activeOrder = event.player.persistentData.activeOrder
    event.player.give(global.getOrderBookContent(activeOrder))
  }
})