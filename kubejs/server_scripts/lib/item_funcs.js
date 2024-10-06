// priority: 1

const numItemsInPlayer = (player, itemId) => {
  let count = 0
  for (let itemStack of player.inventory.allItems) {
    if (itemStack.id === itemId) {
      count += itemStack.count
    }
  }
  return count
}

const removeItemsInPlayer = (player, itemId, numToRemove) => {
  let numLeftToRemove = numToRemove
  for (let itemStack of player.inventory.allItems) {
    if (itemStack.id === itemId) {
      if (itemStack.count <= numLeftToRemove) {
        numLeftToRemove -= itemStack.count
        itemStack.count = 0
      } else {
        itemStack.count -= numLeftToRemove
        numLeftToRemove = 0
      }
      if (numLeftToRemove <= 0) {
        break
      }
    }
  }
}
