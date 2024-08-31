ItemEvents.entityInteracted(event => {
  let player = event.player
  let target = event.target
  let handItemId = player.mainHandItem.id
  if (canSellDishesTo(target)) {
    if (global.isItemAMenu(handItemId)) {
      let activeOrder = player.persistentData.activeOrder
      if (activeOrder) {
        tellPlayerAlreadyOrdered(player, activeOrder)
      } else {
        setPlayerOrder(player, target, handItemId)
        givePlayerOrderBook(player)
      }
  
      event.cancel()
    } else if (
      isPlayerHoldingRequestedDish(player) &&
      isEntityActiveCustomer(target, player)
    ) {
      deliverDishForPlayer(player, handItemId)
      player.mainHandItem.count --
      givePlayerOrderBook(player)

      event.cancel()
    }
  }
})

const canSellDishesTo = (entity) => {
  return entity.type === 'minecraft:villager'
}