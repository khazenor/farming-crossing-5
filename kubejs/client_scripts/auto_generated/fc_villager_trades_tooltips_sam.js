ItemEvents.modifyTooltips(event => {
  event.add(
    [
      'aquaculture:fishing_line', 
      'aquaculture:bobber', 
      'aquaculture:tackle_box', 
      'aquaculture:diamond_fishing_rod', 
      'aquaculture:nether_star_hook', 
      'aquaculture:neptunium_ingot'
    ],
    [
      Text.translate('fcCustomVillagers.youCanBuyThisItemFromSam')
    ])

})