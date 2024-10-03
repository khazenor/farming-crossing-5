StartupEvents.registry('item', event => {
  event.create('kubejs:tuna_akami')
  event.create('kubejs:tuna_chutoro')
  event.create('kubejs:tuna_otoro')

  simpleFood(event, 'sashimi_akami', 4, 1)
  simpleFood(event, 'sashimi_chutoro', 4, 1.5)
  simpleFood(event, 'sashimi_otoro', 4, 2)

  simpleFood(event, 'nigiri_akami', 6, 1)
  simpleFood(event, 'nigiri_chutoro', 7, 1.5)
  simpleFood(event, 'nigiri_otoro', 8, 2)

  simpleFood(event, 'nigiri_plate', 16, 1.5)
})

const simpleFood = (event, id, nutrition, saturation) => {
  event.create(`kubejs:${id}`).food(food => {
    food
      .nutrition(nutrition)
      .saturation(saturation)
  })
}