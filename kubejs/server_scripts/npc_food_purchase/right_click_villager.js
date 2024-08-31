ItemEvents.entityInteracted(event => {
  let handItemId = event.player.mainHandItem.id
  if (global.isItemAMenu(handItemId)) {
    let player = event.player
    let activeOrder = event.player.persistentData.activeOrder
    if (activeOrder) {
      tellPlayerAlreadyOrdered(player, activeOrder)
    } else {
      setPlayerOrder(player, event.target, handItemId)
      givePlayerOrderBook(player)
    }
  }
})

const tellPlayerAlreadyOrdered = (player, activeOrder) => {
  player.tell(global.getFormattedTran('npcFoodPurchase.alreadyHaveOrderFrom',[
    global.genStrFromPlayerObj(
      activeOrder.customerName
    )
  ]))
}

const setPlayerOrder = (player, target, menuId) => {
  let order = global.getOrderObject(
    target,
    menuId
  )
  player.persistentData.activeOrder = order
}

const givePlayerOrderBook = (player) => {
  let activeOrder = player.persistentData.activeOrder
  player.give(global.getOrderBookContent(activeOrder))
}