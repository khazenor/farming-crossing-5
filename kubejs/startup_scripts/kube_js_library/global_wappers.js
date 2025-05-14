// priority: -1
global.RecipeViewerEventsAddInformationItem = (event) => {
  let requests = RequestHandler.jei.infoForItemCache
  for (let request of requests) {
    event.add(request[0], request[1])
  }
}

global.ItemEventsModifyTooltips = (event) => {
  RequestHandler.tooltips.addCache.forEach(request => {
    event.add(request[0], request[1])
  })
}

global.ServerEventsTagsItem = (event) => {
  RequestHandler.tags.removeAllFromItemsCache.forEach(
    itemIds => { event.removeAllTagsFrom(itemIds) }
  )

  RequestHandler.tags.addCache.forEach(request => {
    event.add(request[0], request[1])
  })
}
