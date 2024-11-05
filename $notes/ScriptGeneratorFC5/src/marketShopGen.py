from lib import farmingForBlockheads
from lib import util
from lib import kubejs
from input import marketShop
from lib import fcTrans
from src import marketShopEnchantmentGen

transParentKey = 'marketTooltips'

def generateMarketShops():
	fcTrans.setDefaultTranslationParent(transParentKey)
	farmingForBlockheads.remakeDataPack()
	farmingForBlockheads.genMarket(marketShop.categories)
	generateMarketTooltips(marketShop.categories)
	marketShopEnchantmentGen.generateEnchantmentMarket()
	fcTrans.resetDefaultTranslationParent()
	farmingForBlockheads.packMarketZip()

def generateMarketTooltips(categories):
	itemsByPrice = {}
	for categoryKey in categories:
		category = categories[categoryKey]
		for entryGroup in category[marketShop.entryGroupsKey]:
			price = util.defaultDict(entryGroup, marketShop.priceKey, 1)
			for itemId in entryGroup[marketShop.itemsKey]:
				util.addToDictList(itemsByPrice, price, itemId)

	tooltipContent = ""
	for price in itemsByPrice:
		items = itemsByPrice[price]
		if price > 1:
			plural = 's'
		else:
			plural = ''
		tooltip = f"Obtainable for {price} ticket{plural} in the market"
		tooltipContent += kubejs.eventAddTranslatedTooltips(items, [tooltip])
		kubejs.writeClientFile(
			kubejs.tooltipFileContent(tooltipContent),
			'market_tooltips'
		)
