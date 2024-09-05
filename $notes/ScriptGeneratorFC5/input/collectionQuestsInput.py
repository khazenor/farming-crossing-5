filenameKey = 'filename'
iconKey = 'icon'
nameKey = 'name'
dependencyIdKey = 'dependencyId'
increaseRateKey = 'increaseRate'

collectionNotificationKey = 'collectionNotification'

typeKey = 'type'
itemQuestTypeConst = 'itemQuestType'
observationQuestTypeConst = 'observationQuestType'

questGroupsKey = 'questGroups'
tasksKey = 'tasks'
observeKey = 'observe'
additionalRewardsKey = 'additionalRewards'
questStartAtCenterKey = 'questStartAtCenter'

questlineGroupId = '6A7C23160DA2BBC4'

itemSeedStrs = {
}

questlines = [
  { # Cooking collection
    filenameKey: 'cooking_collection',
    nameKey: 'Cooking Collection',
    iconKey: 'farmersdelight:cooking_pot',
    collectionNotificationKey: 'New dish cooked!',
    increaseRateKey: 0.04,
    typeKey: itemQuestTypeConst,
    questStartAtCenterKey: False,
    questGroupsKey: [
      {
        nameKey: 'Sweets (Farmers Delight) Completion',
        iconKey: 'farmersdelight:apple_pie',
        dependencyIdKey: '17C8F49C46E40B53', # Chef's Beginning
        tasksKey: [
            'farmersdelight:apple_pie',
            'farmersdelight:sweet_berry_cheesecake',
            'farmersdelight:chocolate_pie',
            'farmersdelight:sweet_berry_cookie',
            'farmersdelight:honey_cookie',
            'farmersdelight:melon_popsicle',
            'farmersdelight:glow_berry_custard'
        ]
      }, {
        nameKey: 'Salads (Farmers Delight) Completion',
        iconKey: 'farmersdelight:fruit_salad',
        dependencyIdKey: '17C8F49C46E40B53', # Chef's Beginning
        tasksKey: [
            'farmersdelight:fruit_salad',
            'farmersdelight:mixed_salad',
            'farmersdelight:nether_salad'
        ]
      }, {
        nameKey: 'Sandwiches (Farmers Delight) Completion',
        iconKey: 'farmersdelight:egg_sandwich',
        dependencyIdKey: '17C8F49C46E40B53', # Chef's Beginning
        tasksKey: [
            'farmersdelight:egg_sandwich',
            'farmersdelight:chicken_sandwich',
            'farmersdelight:hamburger',
            'farmersdelight:bacon_sandwich'
        ]
      }, {
        nameKey: 'Soups (Farmers Delight) Completion',
        iconKey: 'farmersdelight:beef_stew',
        dependencyIdKey: '17C8F49C46E40B53', # Chef's Beginning
        tasksKey: [
            'farmersdelight:beef_stew',
            'farmersdelight:bone_broth',
            'farmersdelight:chicken_soup',
            'farmersdelight:vegetable_soup',
            'farmersdelight:fish_stew',
            'farmersdelight:pumpkin_soup',
            'farmersdelight:baked_cod_stew'
        ]
      }, {
        nameKey: 'Asian Foods (Farmers Delight) Completion',
        iconKey: 'farmersdelight:dumplings',
        dependencyIdKey: '17C8F49C46E40B53', # Chef's Beginning
        tasksKey: [
            'farmersdelight:dumplings',
            'farmersdelight:fried_rice',
            'farmersdelight:cabbage_rolls'
        ]
      }, {
        nameKey: 'Dinners (Farmers Delight) Completion',
        iconKey: 'farmersdelight:steak_and_potatoes',
        dependencyIdKey: '17C8F49C46E40B53', # Chef's Beginning
        tasksKey: [
            'farmersdelight:steak_and_potatoes',
            'farmersdelight:mutton_wrap',
            'farmersdelight:bacon_and_eggs',
            'farmersdelight:stuffed_potato',
            'farmersdelight:mushroom_rice',
            'farmersdelight:ratatouille'
        ]
      }, {
        nameKey: 'Noodles (Farmers Delight) Completion',
        iconKey: 'farmersdelight:pasta_with_mutton_chop',
        dependencyIdKey: '17C8F49C46E40B53', # Chef's Beginning
        tasksKey: [
            'farmersdelight:pasta_with_meatballs',
            'farmersdelight:pasta_with_mutton_chop',
            'farmersdelight:vegetable_noodles',
            'farmersdelight:squid_ink_pasta',
            'farmersdelight:noodle_soup'
        ]
      }, {
        nameKey: 'BBQ (Farmers Delight) Completion',
        iconKey: 'farmersdelight:barbecue_stick',
        dependencyIdKey: '17C8F49C46E40B53', # Chef's Beginning
        tasksKey: [
            'farmersdelight:barbecue_stick',
            'farmersdelight:grilled_salmon',
            'farmersdelight:roasted_mutton_chops'
        ]
      }, {
        nameKey: 'Large Meals (Farmers Delight) Completion',
        iconKey: 'farmersdelight:roast_chicken_block',
        dependencyIdKey: '17C8F49C46E40B53', # Chef's Beginning
        tasksKey: [
            'farmersdelight:roast_chicken_block',
            'farmersdelight:stuffed_pumpkin_block',
            'farmersdelight:honey_glazed_ham_block',
            'farmersdelight:shepherds_pie_block',
            'farmersdelight:rice_roll_medley_block'
        ]
      }
    ]
  },
  { # Aquarium
    filenameKey: 'aquarium',
    nameKey: 'Aquarium',
    iconKey: 'aquaculture:atlantic_herring',
    collectionNotificationKey: 'New fish caught!',
    increaseRateKey: 0.03,
    typeKey: itemQuestTypeConst,
    questGroupsKey: [
      { # Vanilla
        nameKey: 'Vanilla Completion',
        iconKey: 'minecraft:grass_block',
        dependencyIdKey: '6089F50C4E683D57', # Catching Fishes
        tasksKey: [
          "minecraft:cod",
          "minecraft:salmon",
          "minecraft:tropical_fish",
          "minecraft:pufferfish"
        ]
      },
      { # Freshwater
        nameKey: 'Freshwater Completion',
        iconKey: 'minecraft:water_bucket',
        dependencyIdKey: '6089F50C4E683D57', # Catching Fishes
        tasksKey: [
          "aquaculture:smallmouth_bass",
          "aquaculture:bluegill",
          "aquaculture:brown_trout",
          "aquaculture:carp",
          "aquaculture:catfish",
          "aquaculture:gar",
          "aquaculture:minnow",
          "aquaculture:muskellunge",
          "aquaculture:perch"
        ]
      },
      { # Arid
        nameKey: 'Arid Completion',
        iconKey: 'minecraft:dead_bush',
        dependencyIdKey: '6089F50C4E683D57', # Catching Fishes
        tasksKey: [
          "aquaculture:bayad",
          "aquaculture:boulti",
          "aquaculture:capitaine",
          "aquaculture:synodontis"
        ]
      },
      { # Artic
        nameKey: 'Artic Completion',
        iconKey: 'minecraft:packed_ice',
        dependencyIdKey: '6089F50C4E683D57', # Catching Fishes
        tasksKey: [
          "aquaculture:atlantic_cod",
          "aquaculture:blackfish",
          "aquaculture:pacific_halibut",
          "aquaculture:atlantic_halibut",
          "aquaculture:atlantic_herring",
          "aquaculture:pink_salmon",
          "aquaculture:pollock",
          "aquaculture:rainbow_trout"
        ]
      },
      { # Saltwater
        nameKey: 'Saltwater Completion',
        iconKey: 'minecraft:blue_ice',
        dependencyIdKey: '6089F50C4E683D57', # Catching Fishes
        tasksKey: [
          "aquaculture:jellyfish",
          "aquaculture:red_grouper",
          "aquaculture:tuna"
        ]
      },
      { # Swamp
        nameKey: 'Swamp Completion',
        iconKey: 'minecraft:mangrove_propagule',
        dependencyIdKey: '6089F50C4E683D57', # Catching Fishes
        tasksKey: [
          "aquaculture:box_turtle",
          "aquaculture:leech",
          "aquaculture:goldfish"
        ]
      },
      { # Mushroom
        nameKey: 'Mushroom Completion',
        iconKey: 'minecraft:red_mushroom',
        dependencyIdKey: '6089F50C4E683D57', # Catching Fishes
        tasksKey: [
          "aquaculture:brown_shrooma",
          "aquaculture:red_shrooma"
        ]
      },
      { # Jungle
        nameKey: 'Jungle Completion',
        iconKey: 'minecraft:jungle_sapling',
        dependencyIdKey: '6089F50C4E683D57', # Catching Fishes
        tasksKey: [
          "aquaculture:arapaima",
          "aquaculture:piranha",
          "aquaculture:tambaqui",
          "aquaculture:arrau_turtle"
        ]
      }
    ]
  },
  { # Animals
    filenameKey: 'animal_watching',
    nameKey: 'Animal Watching',
    iconKey: 'minecraft:spyglass',
    collectionNotificationKey: 'New animal observed!',
    increaseRateKey: 0.02,
    typeKey: observationQuestTypeConst,
    questGroupsKey: [
      { # General Water
        nameKey: 'General Water Completion',
        iconKey: 'minecraft:water_bucket',
        dependencyIdKey: '5BB57D9BEC8038FB', # Spotting animals
        tasksKey: [
          {
            iconKey: "minecraft:squid_spawn_egg",
            nameKey: "Spot a squid",
            observeKey: "minecraft:squid"
          },
          {
            iconKey: "minecraft:dolphin_spawn_egg",
            nameKey: "Spot a dolphin",
            observeKey: "minecraft:dolphin"
          }
        ]
      },
      { # Beaches
        nameKey: 'Beaches Completion',
        iconKey: 'artifacts:umbrella',
        dependencyIdKey: '5BB57D9BEC8038FB', # Spotting animals
        tasksKey: [
          {
            iconKey: "minecraft:turtle_spawn_egg",
            nameKey: "Spot a turtle",
            observeKey: "minecraft:turtle"
          }
        ]
      },
      { # Desert
        nameKey: 'Desert Completion',
        iconKey: 'minecraft:dead_bush',
        dependencyIdKey: '5BB57D9BEC8038FB', # Spotting animals
        tasksKey: [
          {
            iconKey: "minecraft:camel_spawn_egg",
            nameKey: "Spot a camel",
            observeKey: "minecraft:camel"
          },
          {
            iconKey: "minecraft:sniffer_spawn_egg",
            nameKey: "Spot a sniffer",
            observeKey: "minecraft:sniffer"
          }
        ]
      },
      { # Forest
        nameKey: 'Forest Completion',
        iconKey: 'minecraft:oak_sapling',
        dependencyIdKey: '5BB57D9BEC8038FB', # Spotting animals
        tasksKey: [
          {
            iconKey: "minecraft:wolf_spawn_egg",
            nameKey: "Spot a wolf",
            observeKey: "minecraft:wolf"
          }
        ]
      },
      { # Jungle
        nameKey: 'Jungle Completion',
        iconKey: 'minecraft:jungle_sapling',
        dependencyIdKey: '5BB57D9BEC8038FB', # Spotting animals
        tasksKey: [
          {
            iconKey: "minecraft:panda_spawn_egg",
            nameKey: "Spot a panda",
            observeKey: "minecraft:panda"
          },
          {
            iconKey: "minecraft:parrot_spawn_egg",
            nameKey: "Spot a parrot",
            observeKey: "minecraft:parrot"
          }
        ]
      },
      { # Mountain
        nameKey: 'Mountain Completion',
        iconKey: 'minecraft:goat_horn',
        dependencyIdKey: '5BB57D9BEC8038FB', # Spotting animals
        tasksKey: [
          {
            iconKey: "minecraft:goat_spawn_egg",
            nameKey: "Spot a Goat",
            observeKey: "minecraft:goat"
          }
        ]
      },
      { # Special
        nameKey: 'Special Completion',
        iconKey: 'minecraft:nether_star',
        dependencyIdKey: '5BB57D9BEC8038FB', # Spotting animals
        tasksKey: [
          {
            iconKey: "minecraft:bee_spawn_egg",
            nameKey: "Spot a bee",
            observeKey: "minecraft:bee"
          },
          {
            iconKey: "minecraft:allay_spawn_egg",
            nameKey: "Spot an allay",
            observeKey: "minecraft:allay"
          },
          {
            iconKey: "minecraft:cat_spawn_egg",
            nameKey: "Spot a cat",
            observeKey: "minecraft:cat"
          }
        ]
      },
      { # Savanna
        nameKey: 'Savanna Completion',
        iconKey: 'minecraft:acacia_sapling',
        dependencyIdKey: '5BB57D9BEC8038FB', # Spotting animals
        tasksKey: [
          {
            iconKey: "minecraft:llama_spawn_egg",
            nameKey: "Spot a llama",
            observeKey: "minecraft:llama"
          },
          {
            iconKey: "minecraft:armadillo_spawn_egg",
            nameKey: "Spot a armadillo",
            observeKey: "minecraft:armadillo"
          }
        ]
      },
      { # Plains
        nameKey: 'Plains Completion',
        iconKey: 'minecraft:poppy',
        dependencyIdKey: '5BB57D9BEC8038FB', # Spotting animals
        tasksKey: [
          {
            iconKey: "minecraft:horse_spawn_egg",
            nameKey: "Spot a horse",
            observeKey: "minecraft:horse"
          },
          {
            iconKey: "minecraft:donkey_spawn_egg",
            nameKey: "Spot a donkey",
            observeKey: "minecraft:donkey"
          }
        ]
      },
      { # Grass
        nameKey: 'Grass Completion',
        iconKey: 'minecraft:grass_block',
        dependencyIdKey: '5BB57D9BEC8038FB', # Spotting animals
        tasksKey: [
          {
            iconKey: "minecraft:pig_spawn_egg",
            nameKey: "Spot a pig",
            observeKey: "minecraft:pig"
          },
          {
            iconKey: "minecraft:chicken_spawn_egg",
            nameKey: "Spot a chicken",
            observeKey: "minecraft:chicken"
          },
          {
            iconKey: "minecraft:rabbit_spawn_egg",
            nameKey: "Spot a rabbit",
            observeKey: "minecraft:rabbit"
          },
          {
            iconKey: "minecraft:sheep_spawn_egg",
            nameKey: "Spot a sheep",
            observeKey: "minecraft:sheep"
          },
          {
            iconKey: "minecraft:cow_spawn_egg",
            nameKey: "Spot a cow",
            observeKey: "minecraft:cow"
          }
        ]
      },
      { # Caves
        nameKey: 'Caves Completion',
        iconKey: 'minecraft:stone',
        dependencyIdKey: '5BB57D9BEC8038FB', # Spotting animals
        tasksKey: [
          {
            iconKey: "minecraft:bat_spawn_egg",
            nameKey: "Spot a bat",
            observeKey: "minecraft:bat"
          },
          {
            iconKey: "minecraft:glow_squid_spawn_egg",
            nameKey: "Spot a glow squid",
            observeKey: "minecraft:glow_squid"
          },
          {
            iconKey: "minecraft:axolotl_spawn_egg",
            nameKey: "Spot an axolotl",
            observeKey: "minecraft:axolotl"
          }
        ]
      },
      { # Snowy
        nameKey: 'Snowy Completion',
        iconKey: 'minecraft:snowball',
        dependencyIdKey: '5BB57D9BEC8038FB', # Spotting animals
        tasksKey: [
          {
            iconKey: "minecraft:polar_bear_spawn_egg",
            nameKey: "Spot a polar bear",
            observeKey: "minecraft:polar_bear"
          },
          {
            iconKey: "minecraft:fox_spawn_egg",
            nameKey: "Spot a fox",
            observeKey: "minecraft:fox"
          }
        ]
      },
      { # Swamp
        nameKey: 'Swamp Completion',
        iconKey: 'minecraft:mangrove_propagule',
        dependencyIdKey: '5BB57D9BEC8038FB', # Spotting animals
        tasksKey: [
          {
            iconKey: "minecraft:frog_spawn_egg",
            nameKey: "Spot a frog",
            observeKey: "minecraft:frog"
          },
          {
            iconKey: "minecraft:tadpole_spawn_egg",
            nameKey: "Spot a tadpole",
            observeKey: "minecraft:tadpole"
          }
        ]
      },
      { # Mushroom
        nameKey: 'Mushroom Completion',
        iconKey: 'minecraft:red_mushroom',
        dependencyIdKey: '5BB57D9BEC8038FB', # Spotting animals
        tasksKey: [
          {
            iconKey: "minecraft:mooshroom_spawn_egg",
            nameKey: "Spot a mooshroom",
            observeKey: "minecraft:mooshroom"
          }
        ]
      }
    ]
  },
{ # Flora collection
    filenameKey: 'flora_compendium',
    nameKey: 'Flora Compendium',
    iconKey: "minecraft:red_tulip",
    collectionNotificationKey: 'New flora collected!',
    increaseRateKey: 0.02,
    typeKey: itemQuestTypeConst,
    questGroupsKey: [
      { # Vanilla Foods
        nameKey: 'Vanilla Foods Completion',
        iconKey: 'minecraft:apple',
        dependencyIdKey: '0EABDA42EA87C46C',
        tasksKey: [
          "minecraft:apple",
          "minecraft:bamboo",
          "minecraft:beetroot_seeds",
          "minecraft:brown_mushroom",
          "minecraft:cactus",
          "minecraft:carrot",
          "minecraft:cocoa_beans",
          "minecraft:glow_berries",
          "minecraft:kelp",
          "minecraft:melon_slice",
          "minecraft:potato",
          "minecraft:pumpkin_seeds",
          "minecraft:pumpkin",
          "minecraft:red_mushroom",
          "minecraft:sugar_cane",
          "minecraft:sweet_berries",
          "minecraft:wheat_seeds"
        ]
      },
      { # Misc Foods
        nameKey: 'Moded Foods Completion',
        iconKey: 'farmersdelight:onion',
        dependencyIdKey: '0EABDA42EA87C46C',
        tasksKey: [
          "farmersdelight:cabbage_seeds",
          "farmersdelight:onion",
          "farmersdelight:rice",
          "farmersdelight:tomato_seeds",
        ]
      },
      { # Vanilla Flower
        nameKey: 'Vanilla Flower Completion',
        iconKey: 'minecraft:red_tulip',
        dependencyIdKey: '0EABDA42EA87C46C',
        tasksKey: [
          "minecraft:allium",
          "minecraft:azure_bluet",
          "minecraft:blue_orchid",
          "minecraft:cornflower",
          "minecraft:dandelion",
          "minecraft:lilac",
          "minecraft:lily_of_the_valley",
          "minecraft:orange_tulip",
          "minecraft:oxeye_daisy",
          "minecraft:peony",
          "minecraft:pink_tulip",
          "minecraft:poppy",
          "minecraft:red_tulip",
          "minecraft:rose_bush",
          "minecraft:sunflower",
          "minecraft:white_tulip",
          "minecraft:wither_rose",
          "minecraft:torchflower_seeds"
        ]
      },
      { # Vanilla Sapling
        nameKey: 'Vanilla Sapling Completion',
        iconKey: 'minecraft:oak_sapling',
        dependencyIdKey: '0EABDA42EA87C46C',
        tasksKey: [
          "minecraft:acacia_sapling",
          "minecraft:azalea",
          "minecraft:birch_sapling",
          "minecraft:cherry_sapling",
          "minecraft:dark_oak_sapling",
          "minecraft:jungle_sapling",
          "minecraft:oak_sapling",
          "minecraft:spruce_sapling",
          "minecraft:mangrove_propagule"
        ]
      },
      { # Misc Flora
        nameKey: 'Misc Flora Completion',
        iconKey: 'minecraft:pink_petals',
        dependencyIdKey: '0EABDA42EA87C46C',
        tasksKey: [
          "minecraft:flowering_azalea",
          "minecraft:moss_block",
          "minecraft:moss_carpet",
          "minecraft:pink_petals",
          "minecraft:spore_blossom",
          "minecraft:big_dripleaf",
          "minecraft:sea_pickle",
          "minecraft:lily_pad"
        ]
      }
    ]
  },
  { # Mineral Museum
    filenameKey: 'mineral_museum',
    nameKey: 'Mineral Museum',
    iconKey: 'minecraft:raw_gold',
    collectionNotificationKey: 'New mineral mined!',
    increaseRateKey: 0.03,
    typeKey: itemQuestTypeConst,
    questGroupsKey: [
      { # Vanilla Blocks
        nameKey: 'Vanilla Blocks Completion',
        iconKey: 'minecraft:andesite',
        dependencyIdKey: '44DB551B93AA28F9',
        increaseRateKey: 0.01,
        tasksKey: [
          "minecraft:cobblestone",
          "minecraft:mossy_cobblestone",
          "minecraft:cobbled_deepslate",
          "minecraft:diorite",
          "minecraft:granite",
          "minecraft:andesite",
          "minecraft:sandstone",
          "minecraft:red_sandstone",
          "minecraft:calcite",
          "minecraft:dripstone_block",
          "minecraft:pointed_dripstone",
          "minecraft:smooth_basalt",
          "minecraft:tuff",
          "minecraft:obsidian"
        ]
      },
      { # Ore
        nameKey: 'Ore Completion',
        iconKey: 'minecraft:raw_iron',
        dependencyIdKey: '44DB551B93AA28F9',
        increaseRateKey: 0.03,
        tasksKey: [
          "minecraft:coal",
          "minecraft:raw_copper",
          "minecraft:raw_iron",
          "minecraft:amethyst_shard",
          "minecraft:raw_gold",
          "minecraft:redstone",
          "minecraft:lapis_lazuli",
          "minecraft:diamond"
        ]
      }
    ]
  }
]