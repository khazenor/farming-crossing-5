// Listen to item registry event
StartupEvents.registry('item', event => {
  // The texture for this item has to be placed in kubejs/assets/kubejs/textures/item/test_item.png
  // If you want a custom item model, you can create one in Blockbench and put it in kubejs/assets/kubejs/models/item/test_item.json
  event.create('kubejs:miles_ticket').displayName('Miles Ticket').maxStackSize(100)
  event.create('kubejs:miles_booklet').displayName('Miles Booklet').maxStackSize(100)
	event.create('kubejs:debug').displayName('Debug Item')
  event.create('kubejs:remove_active_order').displayName('Debug: remove active order')
})