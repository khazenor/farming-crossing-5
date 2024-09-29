// prints all foods in the pack

ItemEvents.modification(event => {
  event.modify(/.*/, itemEvent => {
    let item = itemEvent.item()
    let foodProperties = itemEvent.item().defaultInstance.getFoodProperties(null)
    if (foodProperties) {
      if (foodProperties.saturationModifier < .7) {
        console.log(`Light: ${item.id}`)
      } else if (foodProperties.saturationModifier > 1.2) {
        console.log(`Heavy: ${item.id}`)
      } else {
        console.log(`Neither: ${item.id}`)
      }
    }
  })
})