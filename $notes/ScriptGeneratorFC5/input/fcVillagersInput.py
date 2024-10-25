from src import const

nameKey = 'nameKey'
textureKey = 'textureKey'

tradesKey = 'tradesKey'
springTradesKey = 'spring'
summerTradesKey = 'summer'
fallTradesKey = 'fall'
winterTradesKey = 'winter'
villagerItems = 'villagerItems'
villagerNum = 'villagerNum'
playerItems = 'playerItems'
playerNum = 'playerNum'

villagers = [
  {  # Jess
    nameKey: "Jess",
    textureKey: '[I; -1077848691, -1208995402, -1654514684, -235233041]',
    tradesKey: [
      {
        villagerItems: ["mobcapturingtool:mob_capturing_tool"],
        playerNum: 16
      },
      {
        villagerItems: ["packingtape:tape"],
        playerNum: 4
      },
      {
        villagerItems: ["sophisticatedbackpacks:gold_backpack"],
        playerNum: 70
      },
      {
        villagerItems: [
          "sophisticatedbackpacks:diamond_backpack",
          "expandedstorage:wood_to_diamond_conversion_kit",
          "sophisticatedstorage:basic_to_diamond_tier_upgrade"
        ],
        playerNum: 150
      },
      {
        villagerItems: ["waystones:warp_stone"],
        playerNum: 8,
        villagerNum: 2
      },
      {
        villagerItems: ["waystones:waystone"],
        playerNum: 10
      },
      {
        villagerItems: ["minecraft:minecart"],
        playerNum: 4
      },
      {
        villagerItems: ["minecraft:rail"],
        villagerNum: 50
      },
      {
        villagerItems: ["minecraft:powered_rail"],
        villagerNum: 50
      }
    ]
  },
  { # Sam
    nameKey: "Sam",
    textureKey: '[I; 1148917178, -726847179, -1346740860, -103785218]',
    tradesKey: [
      {
        villagerItems: ['aquaculture:fishing_line', 'aquaculture:bobber']
      },
      {
        villagerItems: ['aquaculture:tackle_box'],
        playerNum: 8
      },
      {
        villagerItems: ['aquaculture:diamond_fishing_rod'],
        playerNum: 50
      },
      {
        villagerItems: ['aquaculture:nether_star_hook'],
        playerNum: 75
      },
      {
        villagerItems: ['aquaculture:neptunium_ingot'],
        playerNum: 75
      }
    ]
  },
  { # Pamela
    nameKey: "Pamela",
    textureKey: '[I; 1719854737, -330548725, -1320141960, -835272280]',
    tradesKey: [
      {
        villagerItems: [
          'minecraft:sugar',
          'minecraft:egg',
          'minecraft:bread',
          'farmersdelight:wheat_dough',
          'refurbished_furniture:sea_salt'
        ],
        villagerNum: 16
      },
      {
        villagerItems: ['minecraft:honey_bottle'],
        playerNum: 2
      },
      {
        villagerItems: ['farmersdelight:netherite_knife'],
        playerNum: 50
      }
    ]
  },
  { # Bernina
    nameKey: "Bernina",
    textureKey: '[I; -1878865175, -1859568351, -1885409804, -1118268087]',
    tradesKey: [
      {
        villagerItems: [
          "usefulhats:stocking_cap"
        ]
      },
      {
        villagerItems: [
          "usefulhats:bunny_ears"
        ],
        playerNum: 40
      },
      {
        villagerItems: [
          "usefulhats:straw_hat",
          "usefulhats:ender_helmet",
          "usefulhats:wing_helmet"
        ],
        playerNum: 100
      },
      {
        villagerItems: [
          "usefulhats:lucky_hat",
          "usefulhats:postman_hat",
          "usefulhats:aquanaut_helmet",
          "usefulhats:halo",
        ],
        playerNum: 200
      },
      {
        villagerItems: [
          "usefulhats:chopping_hat",
          "usefulhats:mining_hat",
        ],
        playerNum: 300
      },
      {
        villagerItems: [
          "usefulhats:shulker_helmet"
        ],
        playerNum: 400
      }
    ]
  },
  { # Ren
    nameKey: "Ren",
    textureKey: '[I; -903386511, -1993461572, -1126401121, -494593848]',
    tradesKey: [
      {
        villagerItems: ["kubejs:diamond_ingot"],
        playerNum: 100
      },
      {
        villagerItems: ["minecraft:netherite_upgrade_smithing_template"],
        playerNum: 100
      },
      { 
        villagerItems: ["minecraft:netherite_ingot"],
        playerNum: 500
      },
      { 
        villagerItems: ["advancednetherite:netherite_iron_ingot"],
        playerNum: 1000
      },
      { 
        villagerItems: ["advancednetherite:netherite_gold_ingot"],
        playerNum: 1500
      },
      { 
        villagerItems: ["advancednetherite:netherite_emerald_ingot"],
        playerNum: 2500
      },
      { 
        villagerItems: ["advancednetherite:netherite_diamond_ingot"],
        playerNum: 4000
      }
    ]
  }
]
