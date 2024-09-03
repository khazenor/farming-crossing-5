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
componentsKey = 'components'

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

enchantments = {
  "farmersdelight:backstabbing": 3,
  "minecraft:aqua_affinity": 1,
  "minecraft:bane_of_arthropods": 5,
  "minecraft:binding_curse": 1,
  "minecraft:blast_protection": 4,
  "minecraft:breach": 4,
  "minecraft:channeling": 1,
  "minecraft:density": 5,
  "minecraft:depth_strider": 3,
  "minecraft:efficiency": 5,
  "minecraft:feather_falling": 4,
  "minecraft:fire_aspect": 2,
  "minecraft:fire_protection": 4,
  "minecraft:flame": 1,
  "minecraft:fortune": 3,
  "minecraft:frost_walker": 2,
  "minecraft:impaling": 5,
  "minecraft:infinity": 1,
  "minecraft:knockback": 2,
  "minecraft:looting": 3,
  "minecraft:loyalty": 3,
  "minecraft:luck_of_the_sea": 2,
  "minecraft:lure": 3,
  "minecraft:mending": 1,
  "minecraft:multishot": 1,
  "minecraft:piercing": 4,
  "minecraft:power": 5,
  "minecraft:projectile_protection": 4,
  "minecraft:protection": 4,
  "minecraft:punch": 2,
  "minecraft:quick_charge": 3,
  "minecraft:respiration": 3,
  "minecraft:riptide": 3,
  "minecraft:sharpness": 5,
  "minecraft:silk_touch": 1,
  "minecraft:smite": 5,
  "minecraft:soul_speed": 3,
  "minecraft:sweeping_edge": 3,
  "minecraft:swift_sneak": 3,
  "minecraft:thorns": 3,
  "minecraft:unbreaking": 3,
  "minecraft:vanishing_curse": 1,
  "minecraft:wind_burst": 3
}
