ItemEvents.modifyTooltips(event => {
  event.add(
    [
      'minecraft:glow_ink_sac', 
      'minecraft:ink_sac', 
      'aquaculture:worm', 
      'farmersdelight:salmon_roll', 
      'farmersdelight:cod_roll', 
      'farmersdelight:kelp_roll_slice', 
      'farmersdelight:rice_roll_medley_block', 
      'aquaculture:diamond_fishing_rod', 
      'aquaculture:nether_star_hook', 
      'aquaculture:neptunium_ingot'
    ],
    [
      Text.translate('fcCustomVillagers.youCanBuyThisItemFromSam')
    ])

})