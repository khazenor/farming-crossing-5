const tagItemEventHandler = (event) => {
  tagItemEventHandlerHelper.removeTagsFromItems(event)
}

const tagItemEventHandlerHelper = {
  removeTagsFromItems (event) {
    let removeIds = [].concat(
      EverythingIsCopperFixes.idsToRemoveTagsFrom
    )

    for (let removeId of removeIds) {
      event.removeAllTagsFrom(removeId)
    }
  }
}