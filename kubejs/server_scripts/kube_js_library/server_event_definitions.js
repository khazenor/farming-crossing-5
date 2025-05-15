RecipeViewerEvents.addInformation('item', event => {
  global.RecipeViewerEventsAddInformationItem(event)
})

ServerEvents.tags('item', event => {
  global.ServerEventsTagsItem(event)
})

ServerEvents.recipes(event => {
  global.ServerEventsRecipes(event)
})

ItemEvents.rightClicked(event => {
  global.ItemEventsRightClicked(event)
})