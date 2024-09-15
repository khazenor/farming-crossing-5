const npcTalkToPlayer = (event) => {
  let player = event.player
  let target = event.target
  if (target.type === 'easy_npc:humanoid' &&
    lastActivityMoreThan(player, 'talkToNPC', 5)
  ) {
    let npcName = event.target.name.getString()
    let playerName = player.name.getString()
    let dialog = global.getRandomArrayElement(npcDialogs[npcName])
    dialog = global.replaceAll(dialog, '<player name>', playerName)
    dialog = `<${npcName}> ${dialog}`
    player.tell(dialog)

    event.cancel()
  }
}