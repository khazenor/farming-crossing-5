ItemEvents.rightClicked('minecraft:written_book', event => {
  let player = event.player
  if (
    player.shiftKeyDown &&
    isItemCurrentOrderBook(player, event.item) &&
    playerHasActiveOrder(player)
  ) {
    if (checkAreYouSure(player)) {
      playerTellTrans(player, 'npcFoodPurchase.currentOrderCleared')
      player.mainHandItem.count = 0
      player.persistentData.activeOrder = 'cleared'
    } else {
      playerTellTrans(player, 'npcFoodPurchase.areYouSureClearOrder')
    }
    event.cancel()
  }
})
