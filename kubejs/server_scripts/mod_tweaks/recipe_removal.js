ServerEvents.recipes(event => {
  let recipeRemoval = {
    progressiveFlight: {
      mod: 'progressiveflight'
    },
    advancedNetherite: {
      output: [
        "advancednetherite:netherite_diamond_ingot",
        "advancednetherite:netherite_emerald_ingot",
        "advancednetherite:netherite_gold_ingot",
        "advancednetherite:netherite_iron_ingot"
      ]
    },
    usefulHats: {
      mod: 'usefulhats'
    }
  }

  for (let removalKey in recipeRemoval) {
    event.remove(recipeRemoval[removalKey])
  }
})
