// priority 1
const MilesTickets = {
  get jeiDescription () {
    let startIdx = 0
    let endIdx = 11
    let descriptionList = []
    for (let i = startIdx; i <= endIdx; i++) {
      descriptionList.push(Text.translate(`description.milesTicket.${i}`))
    }
    return descriptionList
  },
  ticketId: 'kubejs:miles_ticket',
  bookletId: 'kubejs:miles_booklet',
  stackSize: 100,
  numStacksToBundle: 1
}

RequestHandler.jei.infoForItem(
  MilesTickets.ticketId, MilesTickets.jeiDescription
)

RequestHandler.items.create.simple([
  MilesTickets.ticketId,
  MilesTickets.bookletId
])

RequestHandler.recipes.add.shapeless([
  [MilesTickets.ticketId, [MilesTickets.bookletId], 100]
])

RequestHandler.callbacks.itemEvents.rightClicked([
  event => {
    let player = event.player
    if (player.shiftKeyDown && event.item === MilesTickets.bookletId) {
      player.mainHandItem.count --
      let ticketItem = Item.of(MilesTickets.ticketId)
      ticketItem.count = 100
      player.give(ticketItem)
    }
  },
  event => {
    if (event.player.shiftKeyDown && event.item === MilesTickets.ticketId) {
      let ticketThresholdForBundling = MilesTickets.stackSize
        * MilesTickets.numStacksToBundle

      while (
        EventHelpers.numItemsInPlayer(event, MilesTickets.ticketId)
          >= ticketThresholdForBundling
      ) {
        EventHelpers.removeItemsFromPlayer(
          event, MilesTickets.ticketId, MilesTickets.stackSize
        )
        EventHelpers.giveItems(event, MilesTickets.bookletId, 1)
      }
    }
  }
])

RequestHandler.tooltips.add([
  [MilesTickets.ticketId, [Text.translate('ticketBundling.shiftToBundle')]],
  [MilesTickets.bookletId, [
    Text.translate('ticketBundling.bookletWorth'),
    Text.translate('ticketBundling.bookletShift')
  ]]
])
