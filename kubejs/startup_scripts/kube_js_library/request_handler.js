// priority: 1
const RequestCache = {
  jei: {
    infoForItems: [],
  },
  tooltips: {
    add: []
  },
  tag: {
    add: [],
    removeAllFromItems: []
  }
}

const RequestHandler = {
  jei: {
    infoForItem (itemId, infoList) {
      RequestCache.jei.infoForItems.push([itemId, infoList])
    }
  },
  tooltips: {
    add (tooltips) {
      RequestCache.tooltips.add = RequestCache.tooltips.add.concat(tooltips)
    }
  },
  tags: {
    add (tagsDefs) {
      RequestCache.tag.add = RequestCache.tag.add.concat(tagsDefs)
    },
    removeAllFromItems (items) {
      RequestCache.tag.removeAllFromItems
        = RequestCache.tag.removeAllFromItems.concat(items)
    }
  }
}