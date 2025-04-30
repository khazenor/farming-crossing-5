const RefinedStorageFixes = {
  itemsToRemoveRecipesFrom: [
    'refinedstorage:16k_storage_disk',
    'refinedstorage:1k_storage_disk',
    'refinedstorage:4k_storage_disk',
    'refinedstorage:64k_storage_disk'
  ],
  get tooltipDefs () {
    return [[
      this.itemsToRemoveRecipesFrom,
      [Text.translate('refinedStorage.disks.tooltip')]
    ]]
  }
}