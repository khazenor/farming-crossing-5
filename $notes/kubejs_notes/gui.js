var arrowLeft = Item.playerHeadFromSkinHash('3866a889e51ca79c5d200ea6b5cfd0a655f32fea38b8138598c72fb200b97b9')
var arrowRight = Item.playerHeadFromSkinHash('dfbf1402a04064cebaa96b77d5455ee93b685332e264c80ca36415df992fb46c')

ItemEvents.rightClicked((event) => {
  if (event.item.id == "gtceu:computer_monitor_cover") {
      // open ui function        
      createui(event, event.player, 0)
  }
})

let createui = (event, player, page) => {
  player.openChestGUI(Text.of(Text.red('testui')), 3, gui => {
      gui.playerSlots = false
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
}