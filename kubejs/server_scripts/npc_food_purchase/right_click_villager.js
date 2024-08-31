ItemEvents.entityInteracted(event => {
  let player = event.player
  let target = event.target
  let handItemId = player.mainHandItem.id
  if (canSellDishesTo(target)) {
    if (global.isItemAMenu(handItemId)) {
      if (playerHasActiveOrder(player)) {
        let activeOrder = player.persistentData.activeOrder
        tellPlayerAlreadyOrdered(player, activeOrder)
      } else {
        setPlayerOrder(player, target, handItemId)
        givePlayerOrderBook(player)
        tellPlayerVillagerOrder(
          player,
          target,
          global.getTransString(global.menuInfo[handItemId].desc)
        )
      }
  
      event.cancel()
    } else if (
      isPlayerHoldingRequestedDish(player) &&
      isEntityActiveCustomer(target, player)
    ) {
      deliverDishForPlayer(player, handItemId)
      player.mainHandItem.count --
      updateOrCreateOrderBookInInventory(player)
      tellPlayerVillagerThankYou(player, target, handItemId)
      rewardPlayerIfOrderIsComplete(player, target)

      event.cancel()
    }
  }
})

const canSellDishesTo = (entity) => {
  return entity.type === 'minecraft:villager'
}