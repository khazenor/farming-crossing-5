const rufdStripping = {
  get strippingRecipeDefs () {
    return this._logs.map(logName => [logName, this._strippedId(logName)])
  },
  _logs: [
    "bamboo_log",
    "baobab_log",
    "blackwood_log",
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
    "small_oak_log",
    "socotra_log",
    "willow_log"
  ],
  _modId: "regions_unexplored",
  _strippedId (logName) {
    return `${this._modId}:stripped_${logName}`
  }
}

FarmersDelightRequests.addStripping(rufdStripping.strippingRecipeDefs)
