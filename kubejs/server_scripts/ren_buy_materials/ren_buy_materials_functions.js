// priority: 1

const shouldRenBuyMaterials = (event) => {
  let targetType = event.target.type
  let entityName = event.target.name.getString()
  let mainHandItem = event.player.mainHandItem
  return (
    targetType === 'easy_npc:humanoid' &&
    entityName === 'Ren' &&
    global.buildingMaterials.includes(mainHandItem.id) &&
    mainHandItem.count === 100
  )
}

const handleRenBuyMaterials = (event) => {
  let player = event.player
  let entityName = event.target.name.getString()
  let mainHandItem = event.player.mainHandItem
  if (checkAreYouSureLike(player, 'sellingSeafood', 10)) {
    mainHandItem.count = 0;
    player.give(Item.of('kubejs:construction_ticket'))
    event.cancel()
  } else {
    let itemName = global.getTranItemName(player.mainHandItem.id)
    player.tell(Text.translatable('renBuyMaterials.areYouSure', entityName, itemName))
    event.cancel()
  }
}