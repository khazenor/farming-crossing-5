global.isItemAMenu = (itemId) => {
  return global.menus.includes(itemId)
}

global.getOrderObject = (entity, menuId) => {
  let customerName = entity.name.getString()
  let orderDesc = global.menuInfo[menuId].desc
  let orderSize = global.menuInfo[menuId].size
  let reward = global.menuInfo[menuId].numTickets
  console.log(`order title: ${orderDesc}`)
  return {
    customerUUID: entity.uuid.toString(),
    customerName: customerName,
    menuId: menuId,
    orderDesc: orderDesc,
    orderSize: orderSize,
    reward: reward,
    requestedDishes: global.getRequestedDishes(menuId),
    completedDishes: []
  }
}

global.getRequestedDishes = (menuId) => {
  let menuInfo = global.menuInfo[menuId]
  return global.getRandomSubArray(global.customerFoods, menuInfo.numDishes)
}