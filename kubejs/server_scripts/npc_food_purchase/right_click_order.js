ItemEvents.rightClicked('kubejs:customer_order', event => {
  let player = event.player
  player.openChestGUI(Text.of(Text.red('testui')), 3, gui => {
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
