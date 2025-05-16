// priority: -1000
global.RecipeViewerEventsAddInformationItem = (event) => {
  let requests = RequestHandler.jei.infoForItemCache
  for (let request of requests) {
    event.add(request[0], request[1])
  }
}

global.ItemEventsEntityInteracted = (event) => {
  RequestHandler.callbacks.itemEvents.entityInteractedCache.forEach(
    eventCallback => { eventCallback(event) }
  )
}

global.ItemEventsRightClicked = (event) => {
  RequestHandler.callbacks.itemEvents.rightClickedCache.forEach(
    eventCallback => { eventCallback(event) }
  )
}

global.ItemEventsModifyTooltips = (event) => {
  RequestHandler.tooltips.addCache.forEach(request => {
    event.add(request[0], request[1])
  })
}

global.ServerEventsTagsItem = (event) => {
  RequestHandler.tags.item.removeAllCache.forEach(
    itemIds => { event.removeAllTagsFrom(itemIds) }
  )

  RequestHandler.tags.item.addCache.forEach(request => {
    event.add(request[0], request[1])
  })
}

global.ServerEventsTagsWorldgenBiome = (event) => {
  RequestHandler.tags.biome.addCache.forEach(def => {
    event.add(def[0], def[1])
  })
}

global.ServerEventsRecipes = (event) => {
  RequestHandler.recipes.add.shapelessCache.forEach(request => {
    let outputId = request[0]
    let ings = request[1]
    let count = ArrayJs.safeAccess(request, 2, 1)
    event.shapeless(`${count}x ${outputId}`, ings)
  })

  RequestHandler.recipes.add.shapedCache.forEach(request => {
    let outputId = request[0]
    let ingGrid = request[1]
    let ingHash = request[2]
    let count = ArrayJs.safeAccess(request, 3, 1)
    event.shaped(`${count}x ${outputId}`, ingGrid, ingHash)
  })

  RequestHandler.recipes.add.allFoodCookingCache.forEach(def => {
    let outputItem = def[0]
    let inputItem = def[1]
    
    event.smelting(outputItem, inputItem)
    event.blasting(outputItem, inputItem)
    event.smoking(outputItem, inputItem)
    event.campfireCooking(outputItem, inputItem)
  })

  RequestHandler.recipes.remove.byRecipeIdCache.forEach(recipeId => {
    event.remove({ id: recipeId })
  })

  RequestHandler.recipes.remove.byItemIdCache.forEach(itemId => {
    event.remove({ output: itemId })
  })

  RequestHandler.recipes.remove.byModCache.forEach(modId => {
    event.remove({ mod: modId })
  })
}


global.compostable = {
  defaultCompostableChance: .3,
  ServerEventsCompostableRecipes (event) {
    for (let compostableDef of RequestHandler.recipes.add.compostableCache) {
      let compostableId = compostableDef[0]
      let compostableChance = ArrayJs.safeAccess(
        compostableDef, 1, this.defaultCompostableChance
      )
      event.add(compostableId, compostableChance)
    }
  },

  ServerEventsGenerateDataBeforeMods (event) {
    let data_map = { values: {} };
    for (let compostableDef of RequestHandler.recipes.add.compostableCache) {
      // Build up compostables data map for NeoForge
      let compostableId = compostableDef[0]
      let compostableChance = ArrayJs.safeAccess(
        compostableDef, 1, this.defaultCompostableChance
      )
      data_map.values[compostableId] = { chance: compostableChance };
    }

    event.json(`neoforge:data_maps/item/compostables.json`, data_map);
  }
}

