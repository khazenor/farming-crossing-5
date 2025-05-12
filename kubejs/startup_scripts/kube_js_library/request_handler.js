// priority: 1
const RequestHandler = {
  RecipeViewerEvents: {
    requestAddItem (itemId, infoList) {
      this.addItemRequests.push([itemId, infoList])
    },
    addItemRequests: []
  }
}