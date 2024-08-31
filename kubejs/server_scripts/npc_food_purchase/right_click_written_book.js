ItemEvents.rightClicked('minecraft:written_book', event => {
  let curBookTitle = global.genStrFromObj(event.item.displayName.getString())
  let player = event.player
  let playerOrderTitle = getPlayerOrderTitle(player)
  if (player.shiftKeyDown && curBookTitle === playerOrderTitle) {
    if (checkAreYouSure(player)) {
      playerTellTrans(player, 'npcFoodPurchase.currentOrderCleared')
      player.mainHandItem.count = 0
      player.persistentData.activeOrder = null
    } else {
      playerTellTrans(player, 'npcFoodPurchase.areYouSureClearOrder')
    }
    event.cancel()
  }
})
