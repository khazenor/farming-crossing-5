
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
      Text.translate(`npcFoodPurchase.menuDesc1NumDishes${numDishes}`),
      Text.translate(`npcFoodPurchase.menuDesc2NumTickets${numTickets}`),
      '',
      Text.translate('npcFoodPurchase.ifYouLooseOrderBook'),
    ])
  }

  event.add('kubejs:customer_order', [
    Text.translatable('npcFoodPurchase.rightClickToOpenOrderGui'),
    '',
    Text.translate('npcFoodPurchase.shiftRightClickToClear')
  ])
})