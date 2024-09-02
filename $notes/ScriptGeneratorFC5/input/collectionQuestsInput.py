from list import collectionQuests as cqlist

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
    iconKey: 'minecraft:diamond',
    collectionNotificationKey: 'New dish cooked!',
    increaseRateKey: 0.04,
    typeKey: itemQuestTypeConst,
    questStartAtCenterKey: True,
    questGroupsKey: [
      ## Lets Do Foods
      { # Oven
        nameKey: 'Oven Recipes Completion',
        iconKey: 'minecraft:paper',
        dependencyIdKey: '417FEC585331CCC1', # profiting chef
        tasksKey: [
          'minecraft:paper',
          'minecraft:stick',
          'minecraft:oak_log',
          'minecraft:oak_wood',
          'minecraft:stripped_oak_log',
          'minecraft:stripped_oak_wood',
          'minecraft:oak_planks',
          'minecraft:oak_stairs',
          'minecraft:oak_slab',
          'minecraft:oak_fence',
          'minecraft:birch_log',
          'minecraft:jungle_log',
          'minecraft:jungle_wood',
          'minecraft:stripped_dark_oak_wood',
          'minecraft:stripped_dark_oak_log',
          'minecraft:dark_oak_wood',
          'minecraft:acacia_button'
        ]
      }, {
        nameKey: 'Test 2',
        iconKey: 'minecraft:coal',
        dependencyIdKey: '417FEC585331CCC1', # profiting chef
        tasksKey: [
          'minecraft:jungle_log',
          'minecraft:jungle_wood'
        ]
      }
    ]
  }
]