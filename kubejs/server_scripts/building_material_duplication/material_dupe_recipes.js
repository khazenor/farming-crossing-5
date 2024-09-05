ServerEvents.recipes(event => {
  let buildingMaterialDupeNum = 32
  for (let buildingMaterial of global.buildingMaterials) {
    event.shapeless(
      `${buildingMaterialDupeNum}x ${buildingMaterial}`, [
        buildingMaterial, 'kubejs:miles_ticket'
      ]
    )
  }
})