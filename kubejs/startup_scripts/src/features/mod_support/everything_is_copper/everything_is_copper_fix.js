const EverythingIsCopperFixes = {
  nuggetId: 'everythingcopper:copper_nugget',
  get idsToRemoveRecipesFrom () {
    return [ this.nuggetId ]
  },
  get idsToRemoveTagsFrom () {
    return [ this.nuggetId ]
  },
  get shapelessRecipes () {
    return [
      ['create:copper_nugget', [ this.nuggetId ]]
    ]
  }
}