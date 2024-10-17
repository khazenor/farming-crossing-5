global.seafoodDishPrices = {
  'kubejs:nigiri_plate': 16,
  'kubejs:fried_catfish_with_cheesy_grits': 16
}

global.seafoodDishes = () => {
  return Object.keys(global.seafoodDishPrices)
}