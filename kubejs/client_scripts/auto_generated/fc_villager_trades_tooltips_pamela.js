ItemEvents.modifyTooltips(event => {
  event.add(
    [
      'minecraft:sugar', 
      'minecraft:egg', 
      'minecraft:bread', 
      'farmersdelight:wheat_dough', 
      'refurbished_furniture:sea_salt', 
      'farmersdelight:netherite_knife'
    ],
    [
      Text.translate('fcCustomVillagers.youCanBuyThisItemFromPamela')
    ])

})