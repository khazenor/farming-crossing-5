// priority: 1
const RequestCache = {
  jeiInfoForItems: [],
  tooltips: [],
  addTags: [],
  removeAllTagsFromItems: []
}

const RequestHandler = {
  requestJeiInfoForItem (itemId, infoList) {
    RequestCache.jeiInfoForItems.push([itemId, infoList])
  },
  requestTooltips (tooltips) {
    RequestCache.tooltips = RequestCache.tooltips.concat(tooltips)
  },
  addTags (tagsDefs) {
    RequestCache.addTags = RequestCache.addTags.concat(tagsDefs)
  },
  removeAllTagsFromItems (items) {
    RequestCache.removeAllTagsFromItems
      = RequestCache.removeAllTagsFromItems.concat(items)
  }
}