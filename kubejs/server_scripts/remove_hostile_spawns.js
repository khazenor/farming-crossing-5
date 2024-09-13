const hostileEntityTypes = [
  "minecraft:zombie",
  "minecraft:blaze",
  "minecraft:cave_spider",
  "minecraft:creeper",
  "minecraft:enderman",
  "minecraft:endermite",
  "minecraft:evoker",
  "minecraft:guardian",
  "minecraft:illusioner",
  "minecraft:phantom",
  "minecraft:pillager",
  "minecraft:ravager",
  "minecraft:slime",
  "minecraft:spider",
  "minecraft:stray",
  "minecraft:strider",
  "minecraft:vindicator",
  "minecraft:warden",
  "minecraft:witch",
  "minecraft:husk",
  "minecraft:skeleton_horse",
  "minecraft:skeleton",
  "minecraft:zombie_villager",
  "minecraft:zombie_horse",
  "minecraft:drowned"
]

EntityEvents.checkSpawn(event => {
  let difficulty = event.level.difficulty
  let isEasyNormal = (
    difficulty === 'NORMAL' ||
    difficulty === 'EASY'
  )
  if (
    hostileEntityTypes.includes(event.entity.type) &&
    isEasyNormal &&
    event.type === 'NATURAL'
  ) {
    event.cancel()
  }
})