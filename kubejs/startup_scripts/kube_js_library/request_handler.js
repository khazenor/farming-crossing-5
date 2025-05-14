// priority: 1
const RequestHandler = {
  jei: {
    infoForItem (itemId, infoList) {
      this.infoForItemCache.push([itemId, infoList])
    },
    infoForItemCache: [],
  },
  tooltips: {
    add (tooltips) {
      this.addCache = this.addCache.concat(tooltips)
    },
    addCache: []
  },
  tags: {
    add (tagsDefs) {
      this.addCache = this.addCache.concat(tagsDefs)
    },
    addCache: [],
    removeAllFromItems (items) {
      this.removeAllFromItemsCache
        = this.removeAllFromItemsCache.concat(items)
    },
    removeAllFromItemsCache: []
  }
}