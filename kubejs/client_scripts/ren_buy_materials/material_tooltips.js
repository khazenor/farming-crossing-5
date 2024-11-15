ItemEvents.modifyTooltips(event => {
  event.add(global.buildingMaterials, [
    Text.translate('renMaterialTrade.tooltip')
  ])

  event.add('kubejs:construction_ticket', [
    Text.translate('constructionTicket.tooltip')
  ])
})