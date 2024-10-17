ServerEvents.recipes(event => {
  simpleCutting(event, 'aquaculture:catfish', 'kubejs:catfish_fillet', 2)

  event.shapeless(
    'kubejs:breaded_catfish_fillet', [
      'kubejs:catfish_fillet',
      'refurbished_furniture:wheat_flour',
      "#c:foods/milk"
    ]
  )

  refurbishedFrying(event, 'kubejs:breaded_catfish_fillet', 'kubejs:fried_catfish')

  farmersCooking(
    event,
    [
      '#c:seeds',
      'refurbished_furniture:wheat_flour',
      'refurbished_furniture:cheese',
    ],
    'kubejs:cheesy_grits',
    1
  )

  event.shapeless(
    'kubejs:fried_catfish_with_cheesy_grits', [
      'kubejs:cheesy_grits',
      'kubejs:fried_catfish'
    ]
  )
})