global.isItemAMenu = (itemId) => {
  return global.menus.includes(itemId)
}

global.getOrderObject = (entity, menuId) => {
  let customerName = entity.name.getString()
  let orderTitle = Text.translate(
    'npcFoodPurchase.orderFor',
    Text.translate(global.menuInfo[menuId].desc),
    customerName
  ) 
  let reward = global.menuInfo[menuId].numTickets
  return {
    customerUUID: entity.uuid.toString(),
    customerName: customerName,
    menuId: menuId,
    orderTitle: orderTitle,
    reward: reward,
    requestedDishes: global.getRequestedDishes(menuId),
    completedDishes: []
  }
}

global.getRequestedDishes = (menuId) => {
  let menuInfo = global.menuInfo[menuId]
  return global.getRandomSubArray(global.customerFoods, menuInfo.numDishes)
}