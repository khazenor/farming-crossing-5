ItemEvents.entityInteracted(event => {
  let targetType = event.target.type
  if ([
    'minecraft:villager',
    'farmingforblockheads:merchant'
  ].includes(targetType)) {
    if (lastActivityMoreThan(event.player, 'handleVillagerFoodPurchase', .1)) {
      handleVillagerFoodPurchase(event)
    } else {
      event.cancel()
    }
  } else if (targetType === 'easy_npc:humanoid') {
    handleNpcInteraction(event)
  }
})