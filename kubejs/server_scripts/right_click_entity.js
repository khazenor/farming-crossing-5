ItemEvents.entityInteracted(event => {
  let player = event.player
  let target = event.target
  let targetType = target.type
  let handItemId = player.mainHandItem.id
  let customerEntityTypes = [
    'minecraft:villager',
    'farmingforblockheads:merchant',
    'easy_npc:humanoid'
  ]

  if (customerEntityTypes.includes(targetType)) {
    if (lastActivityMoreThan(event.player, 'rightClickEntity', .1)) {
      if (global.isItemAMenu(handItemId)) {
        handleMenuInteraction(event)
      } else if (shouldSellSeafood(event)) {
        handleSellingSeafood(event)
      } else if (shouldSubmitMeal(event)) {
        handleMealSubmission(event)
      } else if (shouldRenBuyMaterials(event)) {
        handleRenBuyMaterials(event)
      } else if (targetType === 'easy_npc:humanoid') {
        handleNpcInteraction(event)
      }
    } else {
      event.cancel()
    }
  }
})