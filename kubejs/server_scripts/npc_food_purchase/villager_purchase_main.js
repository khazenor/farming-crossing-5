let lastOrderedTime

const handleVillagerFoodPurchase = (event) => {
  let player = event.player
  let target = event.target
  let handItemId = player.mainHandItem.id
  if (global.isItemAMenu(handItemId)) {
    if (lastOrderedTime != getCurTime()) {
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
      lastOrderedTime = getCurTime()
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