// todo: update this file after right click mechanic is requestified
const FishSelling = {
  sellableSeafood: [
    'kubejs:nigiri_plate',
    'kubejs:fried_catfish_with_cheesy_grits',
    'aquaculturedelight:jellyfish_jelly',
    'aquaculturedelight:bass_stew',
    'aquaculturedelight:fish_chorba',
    'aquaculturedelight:halaszle',
    'aquaculturedelight:fish_and_chips',
    'aquaculturedelight:buckling',
    'aquaculturedelight:baked_pollock_with_carrots',
    'aquaculturedelight:halibut_with_tartar_sauce',
    'aquaculturedelight:turtle_meat_dish',
    'aquaculturedelight:rollmops',
    'aquaculturedelight:fried_perch_roll'
  ]
}
RequestHandler.tags.item.add([
  ['fc:sellable_seafood', FishSelling.sellableSeafood]
])

RequestHandler.tooltips.add([
  [FishSelling.sellableSeafood, Text.translate('tooltips.fishSelling')]
])