const CreateInteg = {
  get copperToZincRecipes () {
    let copperToZincPairs = [
      ['create:zinc_ingot', 'minecraft:copper_ingot'],
      ['create:zinc_ore', 'minecraft:copper_ore'],
      ['create:raw_zinc', 'minecraft:raw_copper']
    ]

    return copperToZincPairs.map(pair => {
      let zinc = pair[0]
      let copper = pair[1]
      let andesite = 'minecraft:andesite'
      return [
        `4x ${zinc}`, [
          copper, copper, andesite, andesite
        ]
      ]
    })
  }
}

RequestHandler.recipes.add.shapeless(
  CreateInteg.copperToZincRecipes
)