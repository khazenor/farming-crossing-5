ItemEvents.rightClicked('kubejs:customer_order', event => {
  let player = event.player
  let order = getPlayerActiveOrder(player)
  let customerName = global.genStrFromObj(order.customerName)
  let orderDesc = global.genStrFromObj(order.orderDesc)
  let title = Text.translate(orderDesc, customerName)

  player.openChestGUI(title, 6, gui => {
      gui.playerSlots = true
      simpleSlot(gui, 0, 0, 'mcwwindows:pink_mosaic_glass_pane', 'npcFoodPurchase.dishesRequested')
      slotItemsFromRow(gui, 1, order.requestedDishes)
      simpleSlot(gui, 0, 3, 'mcwwindows:lime_mosaic_glass_pane', 'npcFoodPurchase.dishesCompleted')
      slotItemsFromRow(gui, 4, order.completedDishes)
  })
})

const simpleSlot = (gui, col, row, itemId, nameTransKey) => {
  gui.slot(col, row, slot => {
      if (nameTransKey.length > 0) {
        slot.item = Item.of(itemId).withCustomName(Text.translate(nameTransKey))
      } else {
        slot.item = Item.of(itemId)
      }
  })
}

const slotItemsFromRow = (gui, row, itemIdsObj) => {
  let itemArr = global.arrFromObj(itemIdsObj)
  for (let i = 0; i < itemArr.length; i++) {
    let itemId = itemArr[i]
    let slotRow = i > 8 ? row + 1 : row
    let slotCol = i > 8 ? i % 9 : i
    simpleSlot(gui, slotCol, slotRow, itemId, '')
  }
}