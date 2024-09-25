ItemEvents.rightClicked('kubejs:remove_active_order', event => {
  let player = event.player
  player.tell('active order:')
  player.tell(player.persistentData.activeOrder)
  player.tell('active order is now set to "cleared"')
  player.persistentData.activeOrder = 'cleared'
})
