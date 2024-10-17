StartupEvents.registry('item', event => {
  event.create('kubejs:catfish_fillet')
  event.create('kubejs:breaded_catfish_fillet')
  simpleFood(event, 'fried_catfish', 6, 1.2)
  simpleFood(event, 'cheesy_grits', 4, 1.5)
  simpleFood(event, 'fried_catfish_with_cheesy_grits', 16, 1.5)
})