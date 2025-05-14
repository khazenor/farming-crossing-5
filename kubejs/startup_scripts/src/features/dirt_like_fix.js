const DirtLikeFix = {
  dirtLikeItemIds: [
    'minecraft:coarse_dirt',
    'regions_unexplored:ashen_dirt',
    'regions_unexplored:peat_coarse_dirt',
    'regions_unexplored:peat_dirt',
    'regions_unexplored:silt_coarse_dirt',
    'regions_unexplored:silt_dirt'
  ],
  dirtId: 'minecraft:dirt',
  get shapelessRecipes () {
    let shapelessRecipes = []

    for (let dirtLikeId of this.dirtLikeItemIds) {
      shapelessRecipes.push([
        this.dirtId,
        [ dirtLikeId ]
      ])
    }
    return shapelessRecipes
  }
}

RequestHandler.recipes.add.shapeless(
  DirtLikeFix.shapelessRecipes
)