ItemEvents.rightClicked('kubejs:check_collection_progress', event => {
  event.server.runCommandSilent(
    `execute at @p[name=${event.player.username}] run function fc_collection:check_collection_scores`
  )
})