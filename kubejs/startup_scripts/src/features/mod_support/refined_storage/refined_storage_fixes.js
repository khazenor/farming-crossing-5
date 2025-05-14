const RefinedStorageFixes = {
  get recipeIdsToRemove () {
    return this._storageDiskAndParts
  },
  get tooltipDefs () {
    return [[
      this._storageDiskAndParts,
      [Text.translate('refinedStorage.disks.tooltip')]
    ]]
  },
  get _storageDiskAndParts () {
    return [].concat(
      this._storageDiskIds,
      this._storagePartIds
    )
  },
  get _storageDiskIds() {
    return this.storageSizes.map(size => {
      return `refinedstorage:${size}k_storage_disk`
    })
  },
  get _storagePartIds () {
    return this.storageSizes.map((size) => {
      return `refinedstorage:${size}k_storage_part`
    })
  },
  storageSizes: [1, 4, 16, 64]
}

RequestHandler.tooltips.add(RefinedStorageFixes.tooltipDefs)