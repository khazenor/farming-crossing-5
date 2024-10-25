ItemEvents.rightClicked('minecraft:diamond', event => {
  let currentHealth = event.player.attributes.getBaseValue('minecraft:generic.max_health')
  event.player.setAttributeBaseValue('minecraft:generic.max_health', currentHealth + 2)
})