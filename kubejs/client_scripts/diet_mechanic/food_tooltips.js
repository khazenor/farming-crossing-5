ItemEvents.modifyTooltips(event => {
  for (let categoryId in global.foodClassifications) {
    let foodItemIds = global.foodClassifications[categoryId]
    let categoryTooltip = [
      Text.translate('craving.tooltip', 
        global.foodClassificationNames[categoryId]
      )
    ]
    event.add(foodItemIds, categoryTooltip)
  }
})
