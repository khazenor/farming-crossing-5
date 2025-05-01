const recipeEventHandler = (event) => {
  recipeEventHandlerHelper.addShapelessRecipes(event)
  recipeEventHandlerHelper.removeRecipes(event)
  recipeEventHandlerHelper.addShapedRecipes(event)
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
      EverythingIsCopperFixes.idsToRemoveRecipesFrom,
      RefinedStorageFixes.itemsToRemoveRecipesFrom
    )

    let modsToRemove = [
      'progressiveflight',
      'usefulhats',
      'flightblocks'

    ]

    let recipeIdsToRemove = [].concat(
      AquacultureDelightFixes.removeRecipeIds
    )

    for (let id of itemsToRemove) {
      event.remove({ output: id })
    }

    for (let mod of modsToRemove) {
      event.remove({ mod: mod })
    }

    for (let recipeId of recipeIdsToRemove) {
      event.remove({ id: recipeId })
    }
  },
  addShapedRecipes (event) {
    let shapedRecipes = [].concat(
      CookingForBlockheadFixes.shapedRecipes
    )

    for (let shapedRecipe of shapedRecipes) {
      event.shaped(shapedRecipe[0], shapedRecipe[1], shapedRecipe[2])
    }
  }
}