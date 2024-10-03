const handleSellingSeafood = (event) => {
  let player = event.player
  let target = event.target
  let handItemId = player.mainHandItem.id
  let itemName = global.getTranItemName(handItemId)

  if (checkAreYouSureLike(player, 'sellingSeafood', 10)) {
    let seafoodPrice = global.seafoodDishPrices[handItemId]
    player.tell(Text.translatable(
      'foodSell.thankYou',
      target.name.getString(),
      itemName,
      `${seafoodPrice}`
    ))
    player.mainHandItem.count --
    player.give(`${seafoodPrice}x kubejs:miles_ticket`)
  } else {
    player.tell(Text.translatable('foodSell.areYouSureSell', itemName))
  }
  event.cancel()
}

const shouldSellSeafood = (event) => {
  let handItemId = event.player.mainHandItem.id
  return global.seafoodDishes().includes(handItemId)
}