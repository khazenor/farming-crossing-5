const EverythingIsCopperInteg = {
  nuggetId: 'everythingcopper:copper_nugget'
}

RequestHandler.recipes.remove.byItemId([
  EverythingIsCopperInteg.nuggetId
])

RequestHandler.recipes.add.shapeless([
  ['create:copper_nugget', [ EverythingIsCopperInteg.nuggetId ]]
])

RequestHandler.tags.removeAllFromItems([
  EverythingIsCopperInteg.nuggetId
])

RequestHandler.tags.add([[
  'chipped:lantern', [
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
]])