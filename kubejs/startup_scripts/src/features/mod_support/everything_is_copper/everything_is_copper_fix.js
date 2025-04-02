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
  },
  tagSpecObj: {
    'chipped:lantern': [
      'everythingcopper:copper_lantern',
      'everythingcopper:copper_soul_lantern',
      'everythingcopper:exposed_copper_lantern',
      'everythingcopper:exposed_copper_soul_lantern',
      'everythingcopper:oxidized_copper_lantern',
      'everythingcopper:oxidized_copper_soul_lantern',
      'everythingcopper:waxed_copper_lantern',
      'everythingcopper:waxed_copper_soul_lantern',
      'everythingcopper:waxed_exposed_copper_lantern',
      'everythingcopper:waxed_exposed_copper_soul_lantern',
      'everythingcopper:waxed_oxidized_copper_lantern',
      'everythingcopper:waxed_oxidized_copper_soul_lantern',
      'everythingcopper:waxed_weathered_copper_lantern',
      'everythingcopper:waxed_weathered_copper_soul_lantern',
      'everythingcopper:weathered_copper_lantern',
      'everythingcopper:weathered_copper_soul_lantern'
    ]
  }
}