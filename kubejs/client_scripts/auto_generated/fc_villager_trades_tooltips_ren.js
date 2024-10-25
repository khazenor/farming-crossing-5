ItemEvents.modifyTooltips(event => {
  event.add(
    [
      'minecraft:netherite_upgrade_smithing_template', 
      'minecraft:netherite_ingot', 
      'advancednetherite:netherite_iron_ingot', 
      'advancednetherite:netherite_gold_ingot', 
      'advancednetherite:netherite_emerald_ingot', 
      'advancednetherite:netherite_diamond_ingot'
    ],
    [
      Text.translate('fcCustomVillagers.youCanBuyThisItemFromRen')
    ])

})