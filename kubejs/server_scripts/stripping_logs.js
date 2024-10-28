ServerEvents.recipes(event => {
  let logsByMod = {
    "regions_unexplored": [
      "alpha_log",
      "ashen_log",
      "bamboo_log",
      "baobab_log",
      "blackwood_log",
      "brimwood_log_magma",
      "brimwood_log",
      "cobalt_log",
      "cypress_log",
      "dead_log",
      "eucalyptus_log",
      "joshua_log",
      "kapok_log",
      "larch_log",
      "magnolia_log",
      "maple_log",
      "mauve_log",
      "palm_log",
      "pine_log",
      "redwood_log",
      "silver_birch_log",
      "small_oak_log",
      "socotra_log",
      "willow_log"
    ]
  }

  for (let modId in logsByMod) {
    let logNames = logsByMod[modId]
    for (let logName of logNames) {
      let logId = `${modId}:${logName}`
      let strippedLogId = `${modId}:stripped_${logName}`

      strippingRecipe(event, logId, strippedLogId)
    }
  }
})