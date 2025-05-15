// priority: -1000
StartupEvents.registry('item', event => {
  RequestHandler.items.create.simpleCache.forEach(itemId => {
    event.create(itemId)
  })
})