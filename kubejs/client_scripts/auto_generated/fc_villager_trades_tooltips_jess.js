ItemEvents.modifyTooltips(event => {
  event.add(
    [
      'mobcapturingtool:mob_capturing_tool', 
      'compostbag:compost_bag', 
      'hangglider:hang_glider', 
      'packingtape:tape', 
      'waystones:warp_plate', 
      'waystones:waystone', 
      'minecraft:minecart', 
      'minecraft:rail', 
      'minecraft:powered_rail', 
      'sophisticatedbackpacks:gold_backpack', 
      'sophisticatedbackpacks:diamond_backpack', 
      'expandedstorage:wood_to_diamond_conversion_kit', 
      'sophisticatedstorage:basic_to_diamond_tier_upgrade', 
      'sophisticatedstorage:diamond_to_netherite_tier_upgrade', 
      'expandedstorage:diamond_to_netherite_conversion_kit'
    ],
    [
      Text.translate('fcCustomVillagers.youCanBuyThisItemFromJess')
    ])

})