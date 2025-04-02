const recipeEventHandler = (event) => {
  recipeEventHandlerHelper.addShapelessRecipes(event)
}
const recipeEventHandlerHelper = {
  addShapelessRecipes (event) {
    let shapelessRecipes = [].concat(
      CreateRecipes.shapelessRecipes()
    )
    for (let shapelessRecipe of shapelessRecipes) {
      EventWrapper.shapeless(event, shapelessRecipe[0], shapelessRecipe[1])
    }
  }
}