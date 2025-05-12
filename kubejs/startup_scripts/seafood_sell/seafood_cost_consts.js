global.seafoodDishPrices = {
  'kubejs:nigiri_plate': 16,
  'kubejs:fried_catfish_with_cheesy_grits': 16,
  'aquaculturedelight:jellyfish_jelly': 4,
  'aquaculturedelight:bass_stew': 3,
  'aquaculturedelight:fish_chorba': 5,
  'aquaculturedelight:halaszle': 5,
  'aquaculturedelight:fish_and_chips': 4,
  'aquaculturedelight:buckling': 2,
  'aquaculturedelight:baked_pollock_with_carrots': 4,
  'aquaculturedelight:halibut_with_tartar_sauce': 5,
  'aquaculturedelight:turtle_meat_dish': 5,
  'aquaculturedelight:rollmops': 2,
  'aquaculturedelight:fried_perch_roll': 2
}

global.seafoodDishes = () => {
  return Object.keys(global.seafoodDishPrices)
}