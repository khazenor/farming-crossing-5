const recipeEventHandler = (event) => {
  recipeEventHandlerHelper.addShapelessRecipes(event)
  recipeEventHandlerHelper.removeRecipes(event)
}

const recipeEventHandlerHelper = {
  addShapelessRecipes (event) {
    let shapelessRecipes = [].concat(
      CreateRecipes.shapelessRecipes(),
      FruitsDelightContainerFix.shapelessRecipes,
      EverythingIsCopperFixes.shapelessRecipes
    )
    for (let shapelessRecipe of shapelessRecipes) {
      EventWrapper.shapeless(event, shapelessRecipe[0], shapelessRecipe[1])
    }
  },
  removeRecipes (event) {
    let itemsToRemove = [].concat(
      AdvancedNetheriteFixes.idsToRemoveRecipes,
      EverythingIsCopperFixes.idsToRemoveRecipesFrom
    )

    let modsToRemove = [
      'progressiveflight',
      'usefulhats',
      'flightblocks'

    ]

    for (let id of itemsToRemove) {
      event.remove({ output: id })
    }

    for (let mod of modsToRemove) {
      event.remove({ mod: mod })
    }
  }
}