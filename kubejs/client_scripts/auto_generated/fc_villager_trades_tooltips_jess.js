ItemEvents.modifyTooltips(event => {
  event.add(
    [
      'mobcapturingtool:mob_capturing_tool', 
      'sophisticatedbackpacks:gold_backpack', 
      'sophisticatedbackpacks:diamond_backpack', 
      'waystones:waystone', 
      'minecraft:minecart', 
      'minecraft:rail', 
      'minecraft:powered_rail'
    ],
    [
      Text.translate('fcCustomVillagers.youCanBuyThisItemFromJess')
    ])

})