ItemEvents.entityInteracted(event => {
  let player = event.player
  let handItemId = player.mainHandItem.id
  if (canSellDishesTo(event.target)) {
    if (global.isItemAMenu(handItemId)) {
      let activeOrder = player.persistentData.activeOrder
      if (activeOrder) {
        tellPlayerAlreadyOrdered(player, activeOrder)
      } else {
        setPlayerOrder(player, event.target, handItemId)
        givePlayerOrderBook(player)
      }
  
      event.cancel()
    } else if (isPlayerHoldingRequestedDish(player)) {
      deliverDishForPlayer(player, handItemId)
      player.mainHandItem.count --
      givePlayerOrderBook(player)
    }
  }
})

const canSellDishesTo = (entity) => {
  return entity.type === 'minecraft:villager'
}