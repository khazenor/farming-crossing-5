ServerEvents.recipes(event => {
  let noOpItemIds = [
    'minecraft:glass_bottle',
	  "minecraft:bowl"
  ]
  for (let noOpItemId of noOpItemIds) {
    event.shapeless(noOpItemId, [noOpItemId])
  }
})