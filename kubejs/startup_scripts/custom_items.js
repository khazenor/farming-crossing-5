// Listen to item registry event
StartupEvents.registry('item', event => {
  // The texture for this item has to be placed in kubejs/assets/kubejs/textures/item/test_item.png
  // If you want a custom item model, you can create one in Blockbench and put it in kubejs/assets/kubejs/models/item/test_item.json
  event.create('kubejs:miles_ticket')
  event.create('kubejs:miles_booklet')
	event.create('kubejs:debug')
  event.create('kubejs:remove_active_order')
})