ItemEvents.rightClicked('kubejs:customer_order', event => {
  let player = event.player
  let order = getPlayerActiveOrder(player)
  let customerName = global.genStrFromObj(order.customerName)
  let orderDesc = global.genStrFromObj(order.orderDesc)
  let title = Text.translate(orderDesc, customerName)
  player.openChestGUI(title, 3, gui => {
      gui.playerSlots = true
      gui.slot(1, 2, slot => {
          slot.item = 'minecraft:diamond'
          slot.leftClicked = e => {
              event.player.sendSystemMessage('§ayummers')
          }
      })
      gui.slot(7, 1, slot => {
          slot.item = 'minecraft:dead_bush'
          slot.leftClicked = e => {
              event.player.sendSystemMessage('§4yuckers')
          }
      })
  })
})
