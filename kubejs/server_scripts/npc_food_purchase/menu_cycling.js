const menus = [
  'kubejs:small_menu',
  'kubejs:medium_menu',
  'kubejs:large_menu',
]

for (let i = 0; i < menus.length; i++) {
  let fromItem = menus[i]
  let toItem = menus[(i+1) % menus.length]
  ItemEvents.rightClicked(fromItem, event => {
    event.player.mainHandItem.count = 0
    event.player.giveInHand(toItem)
  })
}