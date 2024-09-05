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
  "minecraft:zombie_horse"
]

EntityJSEvents.spawnPlacement(event => {
  let Difficulty = Java.loadClass("net.minecraft.world.Difficulty")

  for (let hostileEntity of hostileEntityTypes) {
    event.and(hostileEntity, (entitypredicate, levelaccessor, spawntype, blockpos, randomsource) => {
      if (
        levelaccessor.level.difficulty == Difficulty.NORMAL &&
        levelaccessor.level.dimension == 'minecraft:overworld'
      ) {
        return false
      }
      return true
    })
  }
})