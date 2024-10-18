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
        villagerItems: ["sophisticatedbackpacks:gold_backpack"],
        playerNum: 70
      },
      {
        villagerItems: ["sophisticatedbackpacks:diamond_backpack"],
        playerNum: 150
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
        villagerNum: 8
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
        villagerItems: ['farmersdelight:netherite_knife'],
        playerNum: 50
      }
    ]
  }
]
