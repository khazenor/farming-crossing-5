
ItemEvents.modifyTooltips(event => {
  event.add([
    'kubejs:roasted_brown_mushroom',
    'kubejs:roasted_red_mushroom',
    'minecraft:brown_mushroom',
    'minecraft:red_mushroom'
  ], [Text.translate('tooltip.kubejs.meaty_mushroom')])
})