// priority: -1
global.eventWrappers = {
  RecipeViewerEventsAddInformationItem (event) {
    let requests = RequestHandler.jeiInfoForItems
    for (let request of requests) {
      event.add(request[0], request[1])
    }
  }
}