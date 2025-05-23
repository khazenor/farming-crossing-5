// priority 1
const MilesTickets = {
  jeiDescription: [
    '# Earning Miles Tickets',
    '## Fishing',
    '- Many fishes from Aquaculture can be cooked into meals that can be sold to the villagers directly',
    '- To sell the seafood dishes, approach a customer (villager, fc5 npc, or market merchant) and right clicking them with the dish in your hand',
    '## Cooking',
    '- You can earn tickets by cooking dishes for the villagers!',
    '- Entity types that will work with this mechanic: minecraft villagers and FarmingForBlockhead merchants',
    '## Collection Quests',
    '- You can earn tickets by collecting various items in the game!',
    '- When you complete certain quests you sometimes can unlock collections to complete.  The more items you complete in the collection, the more tickets you will receive as a reward!',
    '- The collections will be listed in the "Collection Quests" chapter group and the collection rewards will be in the "Collection Achievements" chapter',
    '- Whenever you have a lot of achievements completed, you can collect the ticket rewards from all of them at the same time by clicking the "Click to collect all rewards!" button on the top right corner (looks like a bag with an exclamation mark over it)',
  ],
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
