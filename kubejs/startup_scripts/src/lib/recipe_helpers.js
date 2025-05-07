const RecipeHelpers = {
  addShapeless: (event, resultId, resultNum, ingList) => {
    let number = StrHelper.cleanFloor(resultNum)
    event.shapeless(`${number}x ${resultId}`, ingList)

    // if (DebugMode.recipeTreeAnalysis) {
    //   let recipeIngList = []
    //   let duplicateCache = []
    //   for (let ing of ingList) {
    //     let ingName
    //     let ingType
    //     if (ing.includes('#')) {
    //       ingName = ing.replace('#', '')
    //       ingType = 'tag'
    //     } else {
    //       ingName = ing
    //       ingType = 'item'
    //     }
    //     RecipeEventHelper.pushNonRepeatIngs(
    //       recipeIngList,
    //       duplicateCache,
    //       ingName,
    //       ingType
    //     )
    //   }
    //   ArrayHelper.addToObjectArray(
    //     RecipeEventHelper.modpackDefinedIngsByOutput,
    //     resultId,
    //     recipeIngList
    //   )
    // }
  }
}