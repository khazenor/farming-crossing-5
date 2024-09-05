# Hostile mob spawns
- Hostile mob spawn is turned off for overworld under normal difficulty.  Spawners should still work.
  - To spawn hostile mobs, you can change your difficulty to hard, or delete this file: `kubejs\startup_scripts\remove_hostile_spawns.js`
  - Many mob drops from hostile mobs can be purchased in the market

# Item Stacks
- Most items will stack up to 100 in your inventory
  - This is mostly for Miles Tickets so they can be easily groups in to groups of 100.  However, the mod I have access to that modify stacksizes (Stackable127) only increases the stack sizes for all items at the same time.

# Visual Tweaks
- All resource packs in the resource pack folder are included by default. This is so that I can enable resource packs I get from curseforge and have the modpack still pass their moderation system.
  - If you don't want this to be the case you can modify the `[resourcepacks]` section in `config\global_data_and_resourcepacks.toml` to not contain `"resourcepacks/"` (make sure to remove the comma from the line above this)
- Minecraft villagers and FarmingForBlockheads market villager are retextured to animals by default. (from the Farming Crossing 4 resource pack)

# Crafting Tweaks
## Flora Duplication
- You can duplicate many flora items from this modpack using bone meal in the crafting table.
## Building Material Duplication
- You can duplicate many building materials from this modpack by crafting it with a miles ticket in the crafting table.
## Other Crafting Tweaks
- You can craft a farmingForBlockheads market using miles tickets