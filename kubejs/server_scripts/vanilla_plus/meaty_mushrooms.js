ServerEvents.recipes(event => {
  const cookingRecipes = {
    "kubejs:mushroom_patty": "kubejs:cooked_mushroom_patty"
  }

  for (let inputItem in cookingRecipes) {
    let outputItem = cookingRecipes[inputItem]

    event.smelting(outputItem, inputItem)
    event.blasting(outputItem, inputItem)
    event.smoking(outputItem, inputItem)
    event.campfireCooking(outputItem, inputItem)
  }

  event.shapeless("2x kubejs:mushroom_patty", [
    "minecraft:brown_mushroom", "minecraft:brown_mushroom",
    "minecraft:brown_mushroom", "minecraft:brown_mushroom"
  ])

  event.shapeless("2x kubejs:mushroom_patty", [
    "minecraft:red_mushroom", "minecraft:red_mushroom",
    "minecraft:red_mushroom", "minecraft:red_mushroom"
  ])
})
