// Mods interfaced:
// - farmersdelight
// - aquaculture

RequestHandler.tags.item.add([
  // salt for expanded delight
  ['c:dusts/salt', [ 'refurbished_furniture:sea_salt' ]],

  // knives for slicing
  ['refurbished_furniture:tools/knives', [
    "aquaculture:diamond_fillet_knife",
    "aquaculture:gold_fillet_knife",
    "aquaculture:iron_fillet_knife",
    "aquaculture:neptunium_fillet_knife",
    "aquaculture:stone_fillet_knife",
    "aquaculture:wooden_fillet_knife",
    "farmersdelight:diamond_knife",
    "farmersdelight:flint_knife",
    "farmersdelight:golden_knife",
    "farmersdelight:iron_knife",
    "farmersdelight:netherite_knife"
  ]]
])

// compat recipes
RequestHandler.recipes.add.shapeless([
  ['refurbished_furniture:cheese', [
    "refurbished_furniture:sea_salt",
    "farmersdelight:milk_bottle"
  ], 2]
])

RequestHandler.tooltips.add([
  // avoid using recipe book because of crash
  [[
    'refurbished_furniture:dark_stove',
    'refurbished_furniture:light_stove'
  ], [
    Text.translate('modSpecific.mrCrayfishStove1'),
    Text.translate('modSpecific.mrCrayfishStove2')
  ]]
])
