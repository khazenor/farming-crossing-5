
ItemEvents.modifyTooltips(event => {
  event.add('kubejs:miles_ticket', [Text.translate('ticketBundling.shiftToBundle')])
  event.add('kubejs:miles_booklet', [
    Text.translate('ticketBundling.bookletWorth'),
    Text.translate('ticketBundling.bookletShift')
  ])
})