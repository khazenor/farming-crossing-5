const tagItemEventHandler = (event) => {
  tagItemEventHandlerHelper.removeTagsFromItems(event)
  tagItemEventHandlerHelper.addTags(event)
}

const tagItemEventHandlerHelper = {
  removeTagsFromItems (event) {
    let removeIds = [].concat(
      EverythingIsCopperFixes.idsToRemoveTagsFrom
    )

    for (let removeId of removeIds) {
      event.removeAllTagsFrom(removeId)
    }
  },
  addTags (event) {
    let tagSpecObjs = [].concat(
      MinecraftFixes.tags,
      EverythingIsCopperFixes.tagSpecObj
    )

    for (let tagSpecObj of tagSpecObjs) {
      for (let tagName in tagSpecObj) {
        let itemIds = tagSpecObj[tagName]

        event.add(tagName, itemIds)
      }
    }
  }
}