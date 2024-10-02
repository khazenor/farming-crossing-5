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
  }
]
