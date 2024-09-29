ItemEvents.modifyTooltips(event => {
  for (let categoryId in global.foodClassifications) {
    let foodItemIds = global.foodClassifications[categoryId]
    let categoryTooltip = [`${global.foodClassificationNames[categoryId]} food`]
    event.add(foodItemIds, categoryTooltip)
  }
})
