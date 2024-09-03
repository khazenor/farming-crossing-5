const milesTicket = "kubejs:miles_ticket"
const milesBooklet = "kubejs:miles_booklet"

// expanding
ServerEvents.recipes(event => {
  event.shapeless(`100x ${milesTicket}`, [milesBooklet])
})

ItemEvents.rightClicked(milesBooklet, event => {
  let player = event.player
  if (player.shiftKeyDown) {
    player.mainHandItem.count --
    let ticketItem = Item.of(milesTicket)
    ticketItem.count = 100
    player.give(ticketItem)
  }
})

// bundling
ItemEvents.rightClicked(milesTicket, event => {
  if (event.player.shiftKeyDown) {
    const stackSize = 100
    const numStacksToBundle = 1
    let player = event.player
  
    if (numItemsInPlayer(player, milesTicket) >= stackSize * numStacksToBundle) {
      for (let itemStack of player.inventory.allItems) {
        if (itemStack.id === milesTicket && itemStack.count === stackSize) {
          itemStack.count = 0
          player.give(milesBooklet)
        }
      }
    }
  }
})

const numItemsInPlayer = (player, itemId) => {
  let count = 0
  for (let itemStack of player.inventory.allItems) {
    if (itemStack.id === itemId) {
      count += itemStack.count
    }
  }
  return count
}

