
contentKey = "content"
translationKey = "translation"
plankContentKey = "plankContent"
woodKey = "wood"
planksKeys = [
  'plank',
  'trap',
  'fence',
  'gate',
  'torch',
  'roof',
  'window',
  'door',
  'bridge'
]
woodTypesInfo = [
  {
    woodKey: 'acacia',
    contentKey: [
      "minecraft:acacia_log",
      "extradelight:cinnamon_log", "regions_unexplored:eucalyptus_log"
    ],
    plankContentKey: [
      'minecraft:acacia_planks',
      "extradelight:cinnamon_planks", "regions_unexplored:eucalyptus_planks"
    ],
    translationKey: [ "acacia" ]
  }, 
  {
    woodKey: 'birch',
    contentKey: [
      "minecraft:birch_log",
      "regions_unexplored:dead_log",
      "regions_unexplored:palm_log",
      "regions_unexplored:silver_birch_log",
      "regions_unexplored:willow_log"
    ],
    plankContentKey: [
      'minecraft:birch_planks',
      "regions_unexplored:dead_planks",
      "regions_unexplored:palm_planks",
      "regions_unexplored:willow_planks"
    ],
    translationKey: [ "birch", "abedul" ]
  },
  {
    woodKey: 'cherry',
    contentKey: [
      "minecraft:cherry_log",
      "regions_unexplored:mauve_log"
    ],
    plankContentKey: [
      'minecraft:cherry_planks',
      "regions_unexplored:mauve_planks"
    ],
    translationKey: [ "cherry", "cerezo" ]
  }, 
  {
    woodKey: 'dark_oak',
    contentKey: [
      "minecraft:dark_oak_log",
      "regions_unexplored:ashen_log",
      "regions_unexplored:blackwood_log"
    ],
    plankContentKey: [
      "minecraft:dark_oak_planks",
      "regions_unexplored:blackwood_planks"
    ],
    translationKey: [ "dark_oak", "robleosc" ]
  }, 
  {
    woodKey: 'jungle',
    contentKey: [
      "minecraft:jungle_log",
      "regions_unexplored:baobab_log",
      "regions_unexplored:kapok_log",
      "regions_unexplored:pine_log",
      "regions_unexplored:socotra_log"
    ],
    plankContentKey: [
      "minecraft:jungle_planks",
      "regions_unexplored:baobab_planks",
      "regions_unexplored:kapok_planks",
      "regions_unexplored:pine_planks",
      "regions_unexplored:socotra_planks"
    ],
    translationKey: [ "jungle", "jungla" ]
  }, 
  {
    woodKey: 'mangrove',
    contentKey: [
      "minecraft:mangrove_log",
      "regions_unexplored:magnolia_log",
      "regions_unexplored:redwood_log"
    ],
    plankContentKey: [
      "minecraft:mangrove_planks",
      "regions_unexplored:magnolia_planks",
      "regions_unexplored:redwood_planks"
    ],
    translationKey: [ "mangrove", "manglar" ]
  },
  {
    woodKey: 'oak',
    contentKey: [
      "minecraft:oak_log",
      "regions_unexplored:alpha_log",
      "regions_unexplored:joshua_log",
      "regions_unexplored:larch_log",
      "regions_unexplored:maple_log",
      "regions_unexplored:small_oak_log"
    ],
    plankContentKey: [
      "minecraft:oak_planks",
      "regions_unexplored:alpha_planks",
      "regions_unexplored:joshua_planks",
      "regions_unexplored:larch_planks",
      "regions_unexplored:maple_planks"
    ],
    translationKey: [ "oak", "roble" ]
  }, 
  {
    woodKey: 'spruce',
    contentKey: [
      "minecraft:spruce_log",
      "regions_unexplored:cypress_log"
    ],
    plankContentKey: [
      "minecraft:spruce_planks",
      "regions_unexplored:cypress_planks"
    ],
    translationKey: [ "spruce", "abeto" ]
  }, 
  {
    woodKey: 'bamboo',
    contentKey: [
      'minecraft:bamboo_block',
      "regions_unexplored:bamboo_log"
    ],
    plankContentKey: ['minecraft:bamboo_planks'],
    translationKey: [ "bamboo" ]
  },
  {
    woodKey: 'crimson',
    contentKey: [
      'minecraft:crimson_stem',
      "regions_unexplored:brimwood_log_magma",
      "regions_unexplored:brimwood_log"
    ],
    plankContentKey: [
      'minecraft:crimson_planks',
      "regions_unexplored:brimwood_planks"
    ],
    translationKey: [ "crimson" ]
  },
  {
    woodKey: 'warped',
    contentKey: [
      'minecraft:warped_stem',
      "regions_unexplored:cobalt_log"
    ],
    plankContentKey: [
      'minecraft:warped_planks',
      "regions_unexplored:cobalt_planks"
    ],
    translationKey: [ "warped" ]
  },
  {
    woodKey: 'palm',
    plankContentKey: ['beachparty:palm_planks', 'biomesoplenty:palm_planks'],
    contentKey: ['beachparty:palm_log', 'biomesoplenty:palm_log'],
    translationKey: ['palm']
  }, 
  {
    woodKey: 'dead',
    plankContentKey: ['biomesoplenty:dead_planks'],
    contentKey: ['biomesoplenty:dead_log'],
    translationKey: ['dead']
  }, 
  {
    woodKey: 'fir',
    plankContentKey: ['biomesoplenty:fir_planks'],
    contentKey: ['biomesoplenty:fir_log'],
    translationKey: ['fir']
  }, 
  {
    woodKey: 'hellbark',
    plankContentKey: ['biomesoplenty:hellbark_planks'],
    contentKey: ['biomesoplenty:hellbark_log'],
    translationKey: ['hellbark']
  }, 
  {
    woodKey: 'jacaranda',
    plankContentKey: ['biomesoplenty:jacaranda_planks'],
    contentKey: ['biomesoplenty:jacaranda_log'],
    translationKey: ['jacaranda']
  }, 
  {
    woodKey: 'magic',
    plankContentKey: ['biomesoplenty:magic_planks'],
    contentKey: ['biomesoplenty:magic_log'],
    translationKey: ['magic']
  }, 
  {
    woodKey: 'mahogany',
    plankContentKey: ['biomesoplenty:mahogany_planks'],
    contentKey: ['biomesoplenty:mahogany_log'],
    translationKey: ['mahogany']
  }, 
  {
    woodKey: 'redwood',
    plankContentKey: ['biomesoplenty:redwood_planks'],
    contentKey: ['biomesoplenty:redwood_log'],
    translationKey: ['redwood']
  }, 
  {
    woodKey: 'umbran',
    plankContentKey: ['biomesoplenty:umbran_planks'],
    contentKey: ['biomesoplenty:umbran_log'],
    translationKey: ['umbran']
  }, 
  {
    woodKey: 'willow',
    plankContentKey: ['biomesoplenty:willow_planks'],
    contentKey: ['biomesoplenty:willow_log'],
    translationKey: ['willow']
  }, 
  {
    woodKey: 'alpine_birch',
    contentKey: ['meadow:alpine_birch_log'],
    translationKey: ['alpine_birch']
  }, 
  {
    woodKey: 'alpine_oak',
    contentKey: ['meadow:alpine_oak_log'],
    translationKey: ['alpine_oak']
  }, 
  {
    woodKey: 'fire',
    contentKey: ['meadow:fire_log'],
    translationKey: ['fire']
  }, 
  {
    woodKey: 'pine',
    plankContentKey: ['meadow:pine_planks'],
    contentKey: ['meadow:pine_log'],
    translationKey: ['pine']
  }
]
