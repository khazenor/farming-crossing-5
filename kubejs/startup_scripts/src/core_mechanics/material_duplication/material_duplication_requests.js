// Requires
// - miles_tickets.js
// - material_list.js

const MaterialDupeReqs = {
  buildingMaterialDupeNum: 50,
  get shaplessDefs () {
    let shapelessDefs = []
    for (let buildingMaterial of MaterialList) {
      shapelessDefs.push([
        buildingMaterial,
        [buildingMaterial, MilesTickets.ticketId],
        this.buildingMaterialDupeNum
      ])
    }
    return shapelessDefs
  }
}

RequestHandler.tooltips.add([
  [MaterialList, [
    Text.translate('building_material_duplication.tooltip')
  ]]
])

RequestHandler.recipes.add.shapeless(MaterialDupeReqs.shaplessDefs)
