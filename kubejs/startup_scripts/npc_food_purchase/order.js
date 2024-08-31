global.isItemAMenu = (itemId) => {
  return global.menus.includes(itemId)
}

global.getOrderObject = (entity, menuId) => {
  let customerName = entity.name.getString()
  let orderTitle = global.getFormattedTran('npcFoodPurchase.orderFor', [
    global.getTransString(global.menuInfo[menuId].desc),
    customerName
  ]) 
  return {
    customerUUID: entity.uuid.toString(),
    customerName: customerName,
    menuId: menuId,
    orderTitle: orderTitle,
    requestedDishes: global.getRequestedDishes(menuId),
    completedDishes: []
  }
}

global.getRequestedDishes = (menuId) => {
  let menuInfo = global.menuInfo[menuId]
  return global.getRandomSubArray(global.customerFoods, menuInfo.numDishes)
}