// priority: 1

const npcTalkToPlayer = (event) => {
  let player = event.player
  let target = event.target
  let npcName = target.name.getString()
  if (target.type === 'easy_npc:humanoid' &&
    lastActivityMoreThan(player, 'talkToNPC', 5)
  ) {
    npcSayDialogToPlayer(player, npcName)
    event.server.runCommandSilent(updateVillagerAroundPlayer(player, npcName.toLowerCase()))
    event.cancel()
  }
}

const npcSayDialogToPlayer = (player, npcName) => {
  let playerName = player.name.getString()
  let dialog = global.getRandomArrayElement(npcInfo(npcName, playerName)[npcName].dialogs)
  player.tell(dialog)
}

const updateVillagerAroundPlayer = (player, villager) => {
  return `execute at @p[name=${player.username}] run function fc_villagers:${villager}_update_trades`
}