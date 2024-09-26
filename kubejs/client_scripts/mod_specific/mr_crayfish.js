
ItemEvents.modifyTooltips(event => {
  // avoid using because of crash
  event.add([
    'refurbished_furniture:dark_stove',
    'refurbished_furniture:light_stove'
  ], [
    Text.translate('modSpecific.mrCrayfishStove1'),
    Text.translate('modSpecific.mrCrayfishStove2')
  ])
})