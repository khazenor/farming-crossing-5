const recipeEventHandler = (event) => {
  recipeEventHandlerHelper.removeRecipes(event) // remove before add
  recipeEventHandlerHelper.addShapelessRecipes(event)
  recipeEventHandlerHelper.addShapedRecipes(event)
}

const recipeEventHandlerHelper = {
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
      AquacultureDelightFixes.removeRecipeIds,
      VanillaPlus.removeRecipeIds
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
  addShapelessRecipes (event) {
    let shapelessRecipes = [].concat(
      CreateRecipes.shapelessRecipes(),
      FruitsDelightContainerFix.shapelessRecipes,
      EverythingIsCopperFixes.shapelessRecipes,
      DirtLikeFix.shapelessRecipes,
      VanillaPlus.shapelessRecipes
    )
    for (let shapelessRecipe of shapelessRecipes) {
      EventWrapper.shapeless(event, shapelessRecipe[0], shapelessRecipe[1])
    }
  },
  addShapedRecipes (event) {
    let shapedRecipes = [].concat(
      CookingForBlockheadFixes.shapedRecipes,
      VanillaPlus.shapedRecipes
    )

    for (let shapedRecipe of shapedRecipes) {
      event.shaped(shapedRecipe[0], shapedRecipe[1], shapedRecipe[2])
    }
  }
}