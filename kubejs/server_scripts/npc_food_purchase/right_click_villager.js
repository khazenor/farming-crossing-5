ItemEvents.entityInteracted(event => {
  let handItemId = event.player.mainHandItem.id
  if (global.isItemAMenu(handItemId) && event.target.type === 'minecraft:villager') {
    let player = event.player
    let activeOrder = event.player.persistentData.activeOrder
    if (activeOrder) {
      tellPlayerAlreadyOrdered(player, activeOrder)
    } else {
      setPlayerOrder(player, event.target, handItemId)
      givePlayerOrderBook(player)
    }

    event.cancel()
  }
})
