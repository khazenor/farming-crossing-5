ItemEvents.modifyTooltips(event => {
  event.add(global.buildingMaterials, [
    Text.translate('building_material_duplication.tooltip')
  ])
})