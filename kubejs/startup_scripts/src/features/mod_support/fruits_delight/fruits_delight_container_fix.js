const FruitsDelightContainerFix = {
  get shapelessRecipes () {
    let noOpItemIds = [
      'minecraft:glass_bottle',
      "minecraft:bowl"
    ]
    let recipes = []
    for (let noOpItemId of noOpItemIds) {
      recipes.push([noOpItemId, [noOpItemId]])
    }
    return recipes
  }
}

RequestHandler.recipes.add.shapeless(
  FruitsDelightContainerFix.shapelessRecipes
)