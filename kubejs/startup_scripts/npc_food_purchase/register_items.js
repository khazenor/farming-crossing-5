// Listen to item registry event
StartupEvents.registry('item', event => {
  event.create('kubejs:small_menu').maxStackSize(1)
  event.create('kubejs:medium_menu').maxStackSize(1)
	event.create('kubejs:large_menu').maxStackSize(1)
  event.create('kubejs:customer_order')
})