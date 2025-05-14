// priority: -1
global.RecipeViewerEventsAddInformationItem = (event) => {
  let requests = RequestCache.jei.infoForItems
  for (let request of requests) {
    event.add(request[0], request[1])
  }
}

global.ItemEventsModifyTooltips = (event) => {
  RequestCache.tooltips.add.forEach(request => {
    event.add(request[0], request[1])
  })
}

global.ServerEventsTagsItem = (event) => {
  RequestCache.tag.removeAllFromItems.forEach(
    itemIds => { event.removeAllTagsFrom(itemIds) }
  )

  RequestCache.tag.add.forEach(request => {
    event.add(request[0], request[1])
  })
}
