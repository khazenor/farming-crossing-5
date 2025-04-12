const EventWrapper = {
  shapeless (event, resultStr, ingArr) {
    event.shapeless(resultStr, ingArr)
  },
  stonecutting (event, outputId, inputTag, outputCount) {
    if (!outputCount) {
      outputCount = 1
    }
    event.stonecutting(`${outputCount}x ${outputId}`, `#${inputTag}`)
  },
  woodcutting (event, outputId, inputTag, outputCount) {
    event.custom({
      type: "corail_woodcutter:woodcutting",
      ingredient: {tag: inputTag},
      result: { id: outputId, count: outputCount }
    })
  }
}