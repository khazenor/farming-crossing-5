const tellPlayerAlreadyOrdered = (player, activeOrder) => {
  player.tell(global.getFormattedTran('npcFoodPurchase.alreadyHaveOrderFrom',[
    global.genStrFromObj(
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
  let activeOrder = getPlayerActiveOrder(player)
  player.give(global.getOrderBookContent(activeOrder))
}

const getPlayerOrderTitle = (player) => {
  let activeOrder = getPlayerActiveOrder(player)
  if (activeOrder) {
    return global.genStrFromObj(activeOrder.orderTitle)
  } else {
    return ""
  }
}

const isPlayerHoldingRequestedDish = (player) => {
  let requestedDishes = getPlayerActiveOrder(player).requestedDishes
  return global.getObjArrIncludes(requestedDishes, player.mainHandItem.id)
}

const getPlayerActiveOrder = (player) => {
  return player.persistentData.activeOrder
}
