ItemEvents.entityInteracted(event => {
  if (lastActivityMoreThan(event.player, 'rightClickedVillager', 0.5)) {
    handleVillagerFoodPurchase(event)
    npcTalkToPlayer(event)
  }
})