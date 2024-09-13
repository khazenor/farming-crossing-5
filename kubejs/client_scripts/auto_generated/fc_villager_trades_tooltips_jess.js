ItemEvents.modifyTooltips(event => {
  event.add(
    [
      'minecraft:diamond', 
      'minecraft:paper', 
      'minecraft:apple'
    ],
    [
      Text.translate('fcCustomVillagers.you_can_buy_this_item_from_jess')
    ])

})