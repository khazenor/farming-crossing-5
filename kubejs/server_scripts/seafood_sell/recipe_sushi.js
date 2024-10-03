ServerEvents.recipes(event => {
  const tunaNames = ['akami', 'chutoro', 'otoro']

  // fillets
  cuttingRecipe(
    event,
    'aquaculture:tuna',
    [
      itemObj('kubejs:tuna_akami', 4),
      itemObj('kubejs:tuna_chutoro', 2),
      itemObj('kubejs:tuna_otoro', 1),
      itemObj('minecraft:bone_meal', 4)
    ]
  )

  // sashimi
  for (let tunaName of tunaNames) {
    simpleCutting(
      event,
      `kubejs:tuna_${tunaName}`,
      `kubejs:sashimi_${tunaName}`,
      2
    )
  }

  // nigiri
  for (let tunaName of tunaNames) {
    event.shapeless(
      `2x kubejs:nigiri_${tunaName}`, [
        `kubejs:sashimi_${tunaName}`,
        `kubejs:sashimi_${tunaName}`,
        'farmersdelight:cooked_rice'
      ]
    )
  }

  // nigiri plate
  event.shapeless(
    'kubejs:nigiri_plate', [
      'kubejs:nigiri_akami',
      'kubejs:nigiri_akami',
      'kubejs:nigiri_akami',
      'kubejs:nigiri_akami',
      'kubejs:nigiri_chutoro',
      'kubejs:nigiri_chutoro',
      'kubejs:nigiri_otoro',
      'minecraft:bowl'
    ]
  )
})

const simpleCutting = (event, input, output, number) => {
  cuttingRecipe(event, input, [itemObj(output, number)])
}

const itemObj = (id, count) => {
  return {
    "item": {
      "id": id,
      "count": count
    }
  }
}

const cuttingRecipe = (event, input, resultArr) => {
  event.custom({
    "type": "farmersdelight:cutting",
    "ingredients": [{ "item": input }],
    "result": resultArr,
    "tool": {
      "tag": "c:tools/knife"
    }
  })
}
