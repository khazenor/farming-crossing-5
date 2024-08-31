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
