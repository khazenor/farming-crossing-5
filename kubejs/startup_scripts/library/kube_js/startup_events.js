// priority: -1000
StartupEvents.registry('item', event => {
  RequestHandler.items.createSimpleCache.forEach(itemId => {
    event.create(itemId)
  })
})