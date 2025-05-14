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

global.ServerEventsRecipes = (event) => {
  RequestHandler.recipes.add.shapelessCache.forEach(request => {
    event.shapeless(request[0], request[1])
  })

  RequestHandler.recipes.add.shapedCache.forEach(request => {
    event.shaped(request[0], request[1], request[2])
  })

  RequestHandler.recipes.remove.byRecipeIdCache.forEach(recipeId => {
    event.remove({ id: recipeId })
  })

  RequestHandler.recipes.remove.byItemIdCache.forEach(itemId => {
    event.remove({ output: itemId })
  })

  RequestHandler.recipes.remove.byModCache.forEach(modId => {
    event.remove({ mod: modId })
  })
}
