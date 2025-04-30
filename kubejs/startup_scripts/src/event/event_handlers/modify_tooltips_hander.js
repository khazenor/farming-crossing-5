const modifyTooltipsHandler = (event) => {
  const tooltipDefs = [].concat(RefinedStorageFixes.tooltipDefs)

  for (let tooltipDef of tooltipDefs) {
    let itemOrItems = tooltipDef[0]
    let tooltips = tooltipDef[1]
    event.add(itemOrItems, tooltips)
  }
}