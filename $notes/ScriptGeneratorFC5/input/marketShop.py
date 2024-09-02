from list import collectionQuests as cqlist
from src import questCollectionReader

fcCategoryKey = 'fc'
floraCategoryKey = 'flora'
farmCategoryKey = 'farm'
miningCategoryKey = 'mining'

nameKey = 'name'
iconKey = 'icon'
entryGroupsKey = 'entryGroups'
itemsKey = 'items'
priceKey = 'price'
priceItemKey = 'priceItem'
productNumKey = 'productNum'
nbtKey = 'nbt'

categories = {
  fcCategoryKey: {
    nameKey: "Farming Crossing Shop",
    iconKey: "minecraft:mangrove_propagule",
    entryGroupsKey: [
      {
        priceKey: 16,
        itemsKey: ["minecraft:villager_spawn_egg"]
      },
      {
        priceKey: 32,
        itemsKey: ["minecraft:wandering_trader_spawn_egg"]
      },
      {
        priceKey: 8,
        itemsKey: ["minecraft:bundle"]
      },
      {
        priceKey: 4,
        itemsKey: ["minecraft:white_bed"]
      }
    ]
  },
  floraCategoryKey: {
    nameKey: "Garden Stand",
    iconKey: "minecraft:poppy",
    entryGroupsKey: [
      {
        priceKey: 8,
        itemsKey: [
          "minecraft:chorus_fruit"
        ]
      },
      { # dyes
        priceKey: 4,
        productNumKey: 8,
        itemsKey: [
          "minecraft:black_dye",
          "minecraft:blue_dye",
          "minecraft:brown_dye",
          "minecraft:cyan_dye",
          "minecraft:gray_dye",
          "minecraft:green_dye",
          "minecraft:light_blue_dye",
          "minecraft:light_gray_dye",
          "minecraft:lime_dye",
          "minecraft:magenta_dye",
          "minecraft:orange_dye",
          "minecraft:pink_dye",
          "minecraft:purple_dye",
          "minecraft:red_dye",
          "minecraft:white_dye",
          "minecraft:yellow_dye"
        ]
      }
    ]
  }
}
