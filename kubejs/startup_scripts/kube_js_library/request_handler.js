// priority: 1
const RequestHandler = {
  requestJeiInfoForItem (itemId, infoList) {
    this.jeiInfoForItems.push([itemId, infoList])
  },
  jeiInfoForItems: []
}