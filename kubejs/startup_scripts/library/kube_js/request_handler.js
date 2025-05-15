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
  },
  recipes: {
    add: {
      shapeless (defs) {
        this.shapelessCache = this.shapelessCache.concat(defs)
      },
      shapelessCache: [],
      shaped (defs) {
        this.shapedCache = this.shapedCache.concat(defs)
      },
      shapedCache: []
    },
    remove: {
      byRecipeId (ids) {
        this.byRecipeIdCache = this.byRecipeIdCache.concat(ids)
      },
      byRecipeIdCache: [],
      byItemId (ids) {
        this.byItemIdCache = this.byItemIdCache.concat(ids)
      },
      byItemIdCache: [],
      byMod (mods) {
        this.byModCache = this.byModCache.concat(mods)
      },
      byModCache: []
    }
  },
  items: {
    createSimple (ids) {
      this.createSimpleCache = this.createSimpleCache.concat(ids)
    },
    createSimpleCache: []
  },
  callbacks: {
    itemEvents: {
      rightClicked (callbacks) {
        this.rightClickedCache = this.rightClickedCache.concat(callbacks)
      },
      rightClickedCache: []
    }
  }
}