const CreateRecipes = {
  shapelessRecipes () {
    return this.copperToZincRecipes()
  },
  copperToZincRecipes () {
    let copperToZincPairs = [
      [CreateConst.itemIds.zincIngot, MinecraftConst.itemIds.copperIngot],
      [CreateConst.itemIds.zincOre, MinecraftConst.itemIds.copperOre],
      [CreateConst.itemIds.zincRaw, MinecraftConst.itemIds.copperRaw]
    ]

    return copperToZincPairs.map(pair => {
      let zinc = pair[0]
      let copper = pair[1]
      let andesite = MinecraftConst.itemIds.andesite
      return [
        `4x ${zinc}`, [
          copper, copper, andesite, andesite
        ]
      ]
    })
  }
}