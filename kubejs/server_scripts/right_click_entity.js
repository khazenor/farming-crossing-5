ItemEvents.entityInteracted(event => {
  let targetType = event.target.type
  if ([
    'minecraft:villager',
    'farmingforblockheads:merchant'
  ].includes(targetType)) {
    handleVillagerFoodPurchase(event)
  } else if (targetType === 'easy_npc:humanoid') {
    handleNpcInteraction(event)
  }
})