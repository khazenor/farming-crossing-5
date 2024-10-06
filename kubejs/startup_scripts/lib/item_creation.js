// priority: 1

// StartupEvents.registry('item', event
const simpleFood = (event, id, nutrition, saturation) => {
  event.create(`kubejs:${id}`).food(food => {
    food
      .nutrition(nutrition)
      .saturation(saturation)
  })
}