const npcInfo = (npcName, playerName) => {
  return {
    "Jess": {
      dialogs: [
        Text.translate("dialog.jessHi1", npcName),
        Text.translate("dialog.jessHi2Player", npcName, playerName),
        Text.translate("dialog.jessHi3", npcName, playerName)
      ]
    }
  }
}