// Listen to item registry event
StartupEvents.registry('item', event => {
  event.create('kubejs:construction_ticket')
})