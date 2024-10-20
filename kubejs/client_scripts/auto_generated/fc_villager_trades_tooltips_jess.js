ItemEvents.modifyTooltips(event => {
  event.add(
    [
      'mobcapturingtool:mob_capturing_tool', 
      'packingtape:tape', 
      'sophisticatedbackpacks:gold_backpack', 
      'sophisticatedbackpacks:diamond_backpack', 
      'expandedstorage:wood_to_diamond_conversion_kit', 
      'sophisticatedstorage:basic_to_diamond_tier_upgrade', 
      'waystones:warp_stone', 
      'waystones:waystone', 
      'minecraft:minecart', 
      'minecraft:rail', 
      'minecraft:powered_rail'
    ],
    [
      Text.translate('fcCustomVillagers.youCanBuyThisItemFromJess')
    ])

})