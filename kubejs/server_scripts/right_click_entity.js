ItemEvents.entityInteracted(event => {
  let target = event.target
  if ([
    'minecraft:villager',
    'farmingforblockheads:merchant',
    'easy_npc:humanoid'
  ].includes(target.type)) {
    handleVillagerFoodPurchase(event)
  }
})