ServerEvents.recipes(event => {
  let buildingMaterialDupeNum = 50
  for (let buildingMaterial of global.buildingMaterials) {
    event.shapeless(
      `${buildingMaterialDupeNum}x ${buildingMaterial}`, [
        buildingMaterial, 'kubejs:miles_ticket'
      ]
    )
  }
})