for (let i = 0; i < global.menus.length; i++) {
  let menus = global.menus
  let fromItem = menus[i]
  let toItem = menus[(i+1) % menus.length]
  ItemEvents.rightClicked(fromItem, event => {
    if (event.player.shiftKeyDown) {
      givePlayerOrderBook(event.player)
    } else {
      event.player.mainHandItem.count = 0
      event.player.giveInHand(toItem)
    }
  })
}