const handleVillagerFoodPurchase = (event) => {
  let player = event.player
  let target = event.target
  let handItemId = player.mainHandItem.id
  if (global.isItemAMenu(handItemId)) {
    if (playerHasActiveOrder(player)) {
      let activeOrder = player.persistentData.activeOrder
      tellPlayerAlreadyOrdered(player, activeOrder)
    } else {
      setPlayerOrder(player, target, handItemId)
      givePlayerOrderItem(player)
      tellPlayerVillagerOrder(
        player,
        target,
        Text.translate(global.menuInfo[handItemId].size)
      )
    }

    event.cancel()
  } else if (
    isPlayerHoldingRequestedDish(player) &&
    isEntityActiveCustomer(target, player)
  ) {
    deliverDishForPlayer(player, handItemId)
    player.mainHandItem.count --
    tellPlayerVillagerThankYou(player, target, handItemId)
    rewardPlayerIfOrderIsComplete(player, target)

    event.cancel()
  }
}