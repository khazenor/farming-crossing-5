ItemEvents.modifyTooltips(event => {
  event.add(
    [
      'kubejs:diamond_ingot', 
      'minecraft:netherite_upgrade_smithing_template', 
      'minecraft:netherite_ingot', 
      'minecraft:nether_star', 
      'advancednetherite:netherite_iron_ingot', 
      'advancednetherite:netherite_gold_ingot', 
      'advancednetherite:netherite_emerald_ingot', 
      'advancednetherite:netherite_diamond_ingot'
    ],
    [
      Text.translate('fcCustomVillagers.youCanBuyThisItemFromRen')
    ])

})