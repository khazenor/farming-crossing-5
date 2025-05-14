RecipeViewerEvents.addInformation('item', event => {
  global.RecipeViewerEventsAddInformationItem(event)
})

ServerEvents.tags('item', event => {
  global.ServerEventsTagsItem(event)
})
