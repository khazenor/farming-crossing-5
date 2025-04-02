const recipeEventHandler = (event) => {
  recipeEventHandlerHelper.addShapelessRecipes(event)
  recipeEventHandlerHelper.removeRecipes(event)
}

const recipeEventHandlerHelper = {
  addShapelessRecipes (event) {
    let shapelessRecipes = [].concat(
      CreateRecipes.shapelessRecipes(),
      FruitsDelightContainerFix.shapelessRecipes
    )
    for (let shapelessRecipe of shapelessRecipes) {
      EventWrapper.shapeless(event, shapelessRecipe[0], shapelessRecipe[1])
    }
  },
  removeRecipes (event) {
    let recipeRemoval = {
      ids: [
        "advancednetherite:netherite_diamond_ingot",
        "advancednetherite:netherite_emerald_ingot",
        "advancednetherite:netherite_gold_ingot",
        "advancednetherite:netherite_iron_ingot",
        'everythingcopper:copper_nugget'
      ],
      mods: [
        'progressiveflight',
        'usefulhats',
        'flightblocks'
      ]
    }

    for (let id of recipeRemoval.ids) {
      event.remove({ output: id })
    }

    for (let mod of recipeRemoval.mods) {
      event.remove({ mod: mod })
    }
  }
}