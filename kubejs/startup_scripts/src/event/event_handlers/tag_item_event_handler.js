const tagItemEventHandler = (event) => {
  tagItemEventHandlerHelper.removeTagsFromItems(event)
}

const tagItemEventHandlerHelper = {
  removeTagsFromItems (event) {
    let removeIds = [
      'everythingcopper:copper_nugget'
    ]

    for (let removeId of removeIds) {
      event.removeAllTagsFrom(removeId)
    }
  }
}