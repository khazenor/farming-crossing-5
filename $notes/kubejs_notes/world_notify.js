// priority: 0

/**
 * Generate Entity Death World Notification
 *
 * @param {Special.EntityType} entityId
 * @param {Special.Item} itemIcon
 * @param {Internal.Color} titleColor
 * @param {Internal.Color} backgroundColor
 * @param {Internal.Color} borderColor
 * @param {Boolean} isDebug
 */
function entityDeathNotify(
  entityId,
  itemIcon,
  titleColor,
  backgroundColor,
  borderColor
) {
  EntityEvents.death(entityId, (event) => {
    const {
      server: { players },
      source: { player: $player },
    } = event;
    if (!$player) return;

    for (const player of players) {
      player.notify({
        itemIcon: itemIcon,
        backgroundColor: backgroundColor,
        borderColor: borderColor,
        outlineColor: borderColor,
        titleShadow: false,
        text: [
          Text.of("！Global Notify - Boss Has Been Killed！\n")
            .color(titleColor)
            .bold(),
          Text.translate(
            `entity.${entityId.namespace}.${entityId.path}`
          ).green(),
          Text.of(" has been killed by "),
          Text.of(player.displayName).gold(),
        ],
      });
    }
  });
}

entityDeathNotify(
  "minecraft:ender_dragon",
  "minecraft:dragon_head",
  "darkPurple",
  0xd9e4ac,
  0x5d1d96
);
entityDeathNotify(
  "minecraft:wither",
  "minecraft:wither_skeleton_skull",
  0xd81e3d,
  0x372027,
  0x1d1316
);
entityDeathNotify(
  "minecraft:warden",
  "minecraft:reinforced_deepslate",
  "darkAqua",
  0x525255,
  0x0c1116
);
entityDeathNotify(
  "minecraft:elder_guardian",
  "minecraft:sponge",
  "darkBlue",
  0x67ada8,
  0x243a34
);