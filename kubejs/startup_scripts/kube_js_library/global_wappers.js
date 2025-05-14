// priority: -1
global.RecipeViewerEventsAddInformationItem = (event) => {
  let requests = RequestHandler.jeiInfoForItems
  for (let request of requests) {
    event.add(request[0], request[1])
  }
}

global.ItemEventsModifyTooltips = (event) => {
  RequestHandler.tooltips.forEach(request => {
    event.add(request[0], request[1])
  })
}