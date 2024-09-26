const npcTalkToPlayer = (event) => {
  let player = event.player
  let target = event.target
  if (target.type === 'easy_npc:humanoid' &&
    lastActivityMoreThan(player, 'talkToNPC', 5)
  ) {
    let npcName = target.name.getString()
    let dialog = global.getRandomArrayElement(npcInfo[npcName].dialogs)
    npcSayDialogToPlayer(npcName, player, dialog)
    event.server.runCommandSilent(updateVillagerAroundPlayer(player, npcName.toLowerCase()))
    event.cancel()
  }
}

const npcSayDialogToPlayer = (npcName, player, dialog) => {
  let playerName = player.name.getString()
  dialog = global.replaceAll(dialog, '<player name>', playerName)
  dialog = `<${npcName}> ${dialog}`
  player.tell(dialog)
}

const updateVillagerAroundPlayer = (player, villager) => {
  console.log(`execute at @p[name=${player.username}] run function fc_villagers:${villager}_update_trades`)
  return `execute at @p[name=${player.username}] run function fc_villagers:${villager}_update_trades`
}