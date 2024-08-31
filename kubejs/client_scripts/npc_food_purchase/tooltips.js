
ItemEvents.modifyTooltips(event => {
  event.add([
    'kubejs:small_menu',
    'kubejs:medium_menu',
    'kubejs:large_menu',
  ], [
    Text.translate('npcFoodPurchase.cycleMenus')
  ])

  let menuInfo = global.menuInfo
  for (let menuId in menuInfo) {
    let numDishes = menuInfo[menuId].numDishes
    let numTickets = menuInfo[menuId].numTickets

    event.add(menuId, [
      '',
      global.getFormattedTran('npcFoodPurchase.menuDesc1NumDishes', [numDishes]),
      global.getFormattedTran('npcFoodPurchase.menuDesc2NumTickets', [numTickets]),
      '',
      global.getTransString('npcFoodPurchase.ifYouLooseOrderBook'),
      '',
      global.getTransString('npcFoodPurchase.shiftRightClickToClear')
    ])
  }
})