// priority: 1
const RequestHandler = {
  requestJeiInfoForItem (itemId, infoList) {
    this.jeiInfoForItems.push([itemId, infoList])
  },
  jeiInfoForItems: [],
  requestTooltips (tooltips) {
    this.tooltips = this.tooltips.concat(tooltips)
  },
  tooltips: []
  
}