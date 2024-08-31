global.isItemAMenu = (itemId) => {
  return global.menus.includes(itemId)
}

global.getOrderObject = (entity, menuId) => {
  return {
    customer: entity,
    menuId: menuId,
    requestedDishes: global.getRequestedDishes(menuId),
    completedDishes: []
  }
}

global.getRequestedDishes = (menuId) => {
  let menuInfo = global.menuInfo[menuId]
  return global.getRandomSubArray(global.customerFoods, menuInfo.numDishes)
}