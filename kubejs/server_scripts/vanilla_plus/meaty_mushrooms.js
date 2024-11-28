ServerEvents.tags('item', event => {
  let tagEntries = [
    {
      tags: [
        'c:raw_materials',
        'c:foods/raw_bacon',
        'c:foods/raw_beef',
        'c:foods/raw_calamari',
        'c:foods/raw_chicken',
        'c:foods/raw_cod',
        'c:foods/raw_duck',
        'c:foods/raw_fish',
        'c:foods/raw_meat',
        'c:foods/raw_mutton',
        'c:foods/raw_pork',
        'c:foods/raw_salmon',
        'c:foods/raw_squid',
        'c:foods/safe_raw_fish'
      ],
      items: [
        "kubejs:mushroom_patty"
      ]
    }, {
      tags: [
        'c:foods/cooked_bacon',
        'c:foods/cooked_beef',
        'c:foods/cooked_chicken',
        'c:foods/cooked_cod',
        'c:foods/cooked_duck',
        'c:foods/cooked_fish',
        'c:foods/cooked_meat',
        'c:foods/cooked_mutton',
        'c:foods/cooked_pork',
        'c:foods/cooked_salmon'
      ],
      items: [
        "kubejs:cooked_mushroom_patty"
      ]
    }
  ]

  for (let tagEntry of tagEntries) {
    for (let rawTag of tagEntry.tags) {
      event.add(rawTag, tagEntry.items)
    }
  }
})

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
