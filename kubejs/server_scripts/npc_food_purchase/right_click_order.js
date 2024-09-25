ItemEvents.rightClicked('kubejs:customer_order', event => {
  let player = event.player
  let order = getPlayerActiveOrder(player)
  let customerName = global.genStrFromObj(order.customerName)
  let orderDesc = global.genStrFromObj(order.orderDesc)
  let title = Text.translate(orderDesc, customerName)

  player.openChestGUI(title, 6, gui => {
      gui.playerSlots = true
      simpleSlot(gui, 0, 0, 'minecraft:writable_book', 'npcFoodPurchase.dishesRequested')
      simpleSlot(gui, 0, 3, 'minecraft:diamond', 'npcFoodPurchase.dishesCompleted')
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