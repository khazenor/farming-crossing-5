ItemEvents.entityInteracted(event => {
  let target = event.target
  if (canSellDishesTo(target)) {
    handleVillagerFoodPurchase(event)
  }
})

const canSellDishesTo = (entity) => {
  return [
    'minecraft:villager',
    'farmingforblockheads:merchant',
    'easy_npc:humanoid'
  ].includes(entity.type) 
}