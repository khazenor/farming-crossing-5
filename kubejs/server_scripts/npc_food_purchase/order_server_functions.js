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

const isEntityActiveCustomer = (entity, player) => {
  let entityUUID = entity.uuid.toString()
  let customerUUID = global.genStrFromObj(
    player.persistentData.activeOrder.customerUUID
  )
  return entityUUID === customerUUID
}

const getPlayerActiveOrder = (player) => {
  return player.persistentData.activeOrder
}

const deliverDishForPlayer = (player, dishId) => {
  let requestedDishes = (global.arrFromObj(
    player.persistentData.activeOrder.requestedDishes
  ))
  let removeIndex = requestedDishes.indexOf(dishId)
  requestedDishes.splice(removeIndex, 1)
  player.persistentData.activeOrder.requestedDishes = requestedDishes
  let completedDishes = (global.arrFromObj(
    player.persistentData.activeOrder.completedDishes
  ))
  completedDishes.push(dishId)
  player.persistentData.activeOrder.completedDishes = completedDishes
}

const isItemCurrentOrderBook = (player, item) => {
  let playerOrderTitle = getPlayerOrderTitle(player)
  let itemName = global.genStrFromObj(item.displayName.getString())
  return playerOrderTitle === itemName
}

const updateOrCreateOrderBookInInventory = (player) => {
  for (let itemStack of player.inventory.allItems) {
    if (isItemCurrentOrderBook(player, itemStack)) {
      itemStack.count = 0
    }
  }
  givePlayerOrderBook(player)
}
