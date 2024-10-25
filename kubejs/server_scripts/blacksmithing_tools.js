ServerEvents.recipes(event => {
  let diamondSmithingRecipes = {
    "#minecraft:pickaxes": "minecraft:diamond_pickaxe",
    "#minecraft:shovels": "minecraft:diamond_shovel",
    "#minecraft:axes": "minecraft:diamond_axe",
    "#minecraft:hoes": "minecraft:diamond_hoe",
    "#minecraft:swords": "minecraft:diamond_sword",
    "#minecraft:head_armor": "minecraft:diamond_helmet",
    "#minecraft:chest_armor": "minecraft:diamond_chestplate",
    "#minecraft:leg_armor": "minecraft:diamond_leggings",
    "#minecraft:foot_armor": "minecraft:diamond_boots",
    "#c:tools/fishing_rod": "aquaculture:diamond_fishing_rod",
  }

  for (let base in diamondSmithingRecipes) {
    event.smithing(
      diamondSmithingRecipes[base],
      "minecraft:flint",
      base,
      "kubejs:diamond_ingot"
    )
  }
  
  event.smithing(
    "aquaculture:neptunium_fishing_rod",
    "minecraft:flint",
    "#c:tools/fishing_rod",
    "aquaculture:neptunium_ingot"
  )
})