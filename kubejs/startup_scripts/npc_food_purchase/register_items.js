// Listen to item registry event
StartupEvents.registry('item', event => {
  event.create('kubejs:small_menu').displayName('Small Menu').maxStackSize(1)
  event.create('kubejs:medium_menu').displayName('Medium Menu').maxStackSize(1)
	event.create('kubejs:large_menu').displayName('Large Menu').maxStackSize(1)
})