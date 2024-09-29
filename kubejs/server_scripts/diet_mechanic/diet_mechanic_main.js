const playerFullFoodLevel = 20
const cravingThreshold = 2
const potionEffectTime = 24000 // 20*20*60
const potionAmplifier = 2
const hasEatenFirstFoodKey = 'hasEatenFirstFoodKey'
const foodCravingCacheKey = 'foodCravingCacheKey'
const disableFoodCravingNotificationKey = 'disableFoodCravingNotificationKey'

const potionEffects = [
  {
    id: 'minecraft:speed',
    name: 'Speed'
  }, {
    id: 'minecraft:haste',
    name: 'Haste'
  }, {
    id: 'minecraft:strength',
    name: 'Strength'
  }, {
    id: 'minecraft:regeneration',
    name: 'Regeneration'
  }, {
    id: 'minecraft:resistance',
    name: 'Resistance'
  }, {
    id: 'minecraft:absorption',
    name: 'Absorption'
  }, {
    id: 'minecraft:luck',
    name: 'Luck'
  }
]

ItemEvents.foodEaten(event => {
  let cravings = playerFoodCravings(event.player)
  let cravingScore = getCravingScore(event.item.id, cravings)
  if (cravingScore === 0 && event.player.foodLevel < playerFullFoodLevel) {
    autoNotifyPlayerCravings(event.player, cravings)
  }
  if (cravingScore > 0) {
    rewardPlayerWithPotionEffects(event.player, cravingScore)
  } else {
    updatePlayerFoodTallies(event.item, event.player)
    givePlayerCheckItemIfFirstTimeEating(event.player)
  }
})

PlayerEvents.tick(event => {
  let foodLevel = event.player.foodLevel
  let playerData = event.player.persistentData
  if (
    foodLevel === playerFullFoodLevel &&
    (!isTruthy(playerData.wasFull) || !playerData.wasFull)
  ) {
    playerData.wasFull = 'true'
  } else if (foodLevel < playerFullFoodLevel && isTruthy(playerData.wasFull)) {
    playerData.wasFull = 'false'
    let cravings = playerFoodCravings(event.player)
    autoNotifyPlayerCravings(event.player, cravings)
  }
})

const isTruthy = (value) => {
  if (!value) {
    return false
  } else if (value === 'true') {
    return true
  } else if (value === 'false') {
    return false
  } else if (defaultToZero(value) === 0) {
    return false
  }
}

ItemEvents.rightClicked('kubejs:check_food_cravings', event => {
  let player = event.player
  if (player.shiftKeyDown) {
    let newDoDisable
    if (player.persistentData[disableFoodCravingNotificationKey] === 'true') {
      newDoDisable = 'false'
    } else {
      newDoDisable = 'true'
    }
    player.persistentData[disableFoodCravingNotificationKey] = newDoDisable
    let onOff = newDoDisable === 'true' ? 'off': 'on'
    player.tell(`Craving notification is now turned ${onOff}`)
  } else {
    player.tell('')
    displayFoodTallies(player)
    let cravings = playerFoodCravings(player)
    if (cravings.length > 0) {
      notifyPlayerOfCravings(player, cravings)
    } else {
      player.tell('You are currently not craving any types of food.')
    }

    if (player.persistentData[disableFoodCravingNotificationKey] === 'true') {
      player.tell('You currently have craving notifications turned off')
    }
  }
})

const givePlayerCheckItemIfFirstTimeEating = (player) => {
  let playerData = player.persistentData
  if (!playerData[hasEatenFirstFoodKey]) {
    player.give('kubejs:check_food_cravings')
    playerData[hasEatenFirstFoodKey] = true
  }
}

const getCravingScore = (itemId, cravings) => {
  let cravingScore = 0
  for (let craving of cravings) {
    if (global.foodClassifications[craving].includes(itemId)) {
      cravingScore++
    }
  }
  return cravingScore
}

const rewardPlayerWithPotionEffects = (player, cravingScore) => {
  let effects = randomSelectFromArr(potionEffects, cravingScore)
  if (cravingScore === 1) {
    player.tell('That was tasty!')
  } else if (cravingScore === 2) {
    player.tell('That was delicious!')
  } else {
    player.tell('That was out of this world!')
  }

  let message = 'The food has given you '

  player.potionEffects.clear()
  for (let i = 0; i<effects.length; i++) {
    let effect = effects[i]
    player.potionEffects.add(
      effect.id,
      potionEffectTime,
      potionAmplifier,
      false,
      false
    )

    if (i > 0 && effects.length > 2) {
      message += ","
    }
    if (i > 0) {
      message += " "
    }
    if (i > 0 && i === effects.length - 1) {
      message += "and "
    }
    message += effect.name
  }
  player.tell(message)

  resetTallies(player)
}

const resetTallies = (player) => {
  for (let foodCategory in global.foodClassifications) {
    player.persistentData[foodCategory] = 0
  }
  player.persistentData[foodCravingCacheKey] = ""
}

const randomSelectFromArr = (arr, numSelect) => {
  let randomElms = []
  for (let i = 0; i<numSelect; i++) {
    let randomElm = arr[Math.floor(Math.random() * arr.length)]
    while (randomElms.includes(randomElm)) {
      randomElm = arr[Math.floor(Math.random() * arr.length)]
    }
    randomElms.push(randomElm)
  }
  return randomElms
}

const autoNotifyPlayerCravings = (player, cravings) => {
  if (player.persistentData[disableFoodCravingNotificationKey] !== 'true' && cravings.length > 0) {
    cravings.sort()
    let cravingKey = concatArrVals(cravings)
    if (player.persistentData[foodCravingCacheKey] !== cravingKey) {
      player.persistentData[foodCravingCacheKey] = cravingKey
      notifyPlayerOfCravings(player, cravings)
    }
  }
}

const notifyPlayerOfCravings = (player, cravings) => {
  let message = "You are currently craving something that is "
  for (let i = 0; i<cravings.length; i++) {
    let craving = cravings[i]
    if (i > 0 && cravings.length > 2) {
      message += ","
    }
    if (i > 0) {
      message += " "
    }
    if (i > 0 && i === cravings.length - 1) {
      message += "or "
    }
    message += global.foodClassificationNames[craving]
  }
  player.tell(message)
}

const playerFoodCravings = (player) => {
  let cravings = []
  addCraving(global.sweet, global.savory, player, cravings)
  addCraving(global.light, global.heavy, player, cravings)
  addCraving(global.hot, global.cold, player, cravings)
  addCraving(global.wet, global.dry, player, cravings)
  return cravings
}

const addCraving = (categoryYing, categoryYang, player, cravings) => {
  let yingVal = playerTally(categoryYing, player)
  let yangVal = playerTally(categoryYang, player)
  if (yingVal >= cravingThreshold && yingVal > yangVal) {
    cravings.push(categoryYang)
  } else if (yangVal >= cravingThreshold && yangVal > yingVal) {
    cravings.push(categoryYing)
  }
}

const updatePlayerFoodTallies = (item, player) => {
  let playerData = player.persistentData
  updateTalliesBasedOnCategories(item.id, playerData)
}

const displayFoodTallies = (player) => {
  let sweet = playerTally(global.sweet, player)
  let savory = playerTally(global.savory, player)
  let light = playerTally(global.light, player)
  let heavy = playerTally(global.heavy, player)
  let hot = playerTally(global.hot, player)
  let cold = playerTally(global.cold, player)
  let wet = playerTally(global.wet, player)
  let dry = playerTally(global.dry, player)
  player.tell('==== RECENT FOODS EATEN ====')
  player.tell(`  Sweet: ${sweet},   Savory: ${savory}`)
  player.tell(`  Light: ${light},   Heavy: ${heavy}`)
  player.tell(`  Hot: ${hot},   Cold: ${cold}`)
  player.tell(`  Wet: ${wet},   Dry: ${dry}`)
  player.tell('============================')
}

const playerTally = (tallySortName, player) => {
  let playerData = player.persistentData
  return defaultToZero(playerData[tallySortName])
}

const defaultToZero = (value) => {
  if (value) {
    return Number(`${value}`.replace('.0d', ''))
  } else {
    return 0
  }
}

const concatArrVals = (array) => {
  let strVals = ""
  for (let val of array) {
    strVals += val
  }
  return strVals
}

const updateTalliesBasedOnCategories = (itemId, playerData) => {
  for (let foodCategory in global.foodClassifications) {
    if (global.foodClassifications[foodCategory].includes(itemId)) {
      incrementPlayerData(foodCategory, playerData)
    }
  }
}

const incrementPlayerData = (propertyName, playerData) => {
  let score = defaultToZero(playerData[propertyName])
  if (score > 0) {
    playerData[propertyName] = score + 1
  } else {
    playerData[propertyName] = 1
  }
}