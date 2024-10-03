ItemEvents.modifyTooltips(event => {
  for (let seafoodDish of global.seafoodDishes()) {
    let price = global.seafoodDishPrices[seafoodDish]
    event.add(seafoodDish, [
      Text.translate('foodSell.tooltip1', `${price}`),
      Text.translate('foodSell.tooltip2'),
    ])
  }

  
  let tunaNames = ['akami', 'chutoro', 'otoro']
  let itemPrefixes = ['tuna', 'sashimi', 'nigiri']
  for (let tunaName of tunaNames) {
    for (let itemPrefix of itemPrefixes) {
      event.add(`kubejs:${itemPrefix}_${tunaName}`, [
        Text.translate(`item.kubejs.${tunaName}_tooltip`)
      ])
    }
  }
})