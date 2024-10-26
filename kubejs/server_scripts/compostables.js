
const compostables = [
  "regions_unexplored:alpha_sapling",
  "regions_unexplored:apple_oak_sapling",
  "regions_unexplored:ashen_sapling",
  "regions_unexplored:bamboo_sapling",
  "regions_unexplored:baobab_sapling",
  "regions_unexplored:blackwood_sapling",
  "regions_unexplored:blue_magnolia_sapling",
  "regions_unexplored:brimwood_sapling",
  "regions_unexplored:cobalt_sapling",
  "regions_unexplored:cypress_sapling",
  "regions_unexplored:dead_pine_sapling",
  "regions_unexplored:dead_sapling",
  "regions_unexplored:enchanted_birch_sapling",
  "regions_unexplored:eucalyptus_sapling",
  "regions_unexplored:flowering_sapling",
  "regions_unexplored:golden_larch_sapling",
  "regions_unexplored:joshua_sapling",
  "regions_unexplored:kapok_sapling",
  "regions_unexplored:larch_sapling",
  "regions_unexplored:magnolia_sapling",
  "regions_unexplored:maple_sapling",
  "regions_unexplored:mauve_sapling",
  "regions_unexplored:orange_maple_sapling",
  "regions_unexplored:palm_sapling",
  "regions_unexplored:pine_sapling",
  "regions_unexplored:pink_magnolia_sapling",
  "regions_unexplored:red_maple_sapling",
  "regions_unexplored:redwood_sapling",
  "regions_unexplored:silver_birch_sapling",
  "regions_unexplored:small_oak_sapling",
  "regions_unexplored:socotra_sapling",
  "regions_unexplored:white_magnolia_sapling",
  "regions_unexplored:willow_sapling"
]

const compostableChance = .3

ServerEvents.compostableRecipes(event => {
  for (let compostable of compostables) {
    event.add(compostable, compostableChance)
    console.log(compostable)
  }
})

ServerEvents.generateData('before_mods', (event) => {
  let data_map = { values: {} };
  for (let compostable of compostables) {
    // Build up compostables data map for NeoForge
    data_map.values[compostable] = { chance: compostableChance };
  }

  event.json(`neoforge:data_maps/item/compostables.json`, data_map);
})