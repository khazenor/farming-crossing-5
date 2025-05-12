const MilesTickets = {
  jeiDescription: [
    'test',
    'test2'
  ],
  ticketId: 'kubejs:miles_ticket'
}

RequestHandler.RecipeViewerEvents.requestAddItem(
  MilesTickets.ticketId, MilesTickets.jeiDescription
)
