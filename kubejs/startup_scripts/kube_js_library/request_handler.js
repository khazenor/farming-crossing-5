// priority: 1
const RequestCache = {
  jeiInfoForItems: [],
  tooltips: []
}

const RequestHandler = {
  requestJeiInfoForItem (itemId, infoList) {
    RequestCache.jeiInfoForItems.push([itemId, infoList])
  },
  requestTooltips (tooltips) {
    RequestCache.tooltips = RequestCache.tooltips.concat(tooltips)
  }
}