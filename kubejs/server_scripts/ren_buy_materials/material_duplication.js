ServerEvents.recipes(event => {
  let buildingMaterialDupeNum = 100
  for (let buildingMaterial of global.buildingMaterials) {
    event.shapeless(
      `${buildingMaterialDupeNum}x ${buildingMaterial}`, [
        buildingMaterial, 'kubejs:construction_ticket'
      ]
    )
  }
})