from lib import easyNpc
from input import fcVillagersInput as vil
from lib import mcfunction
from lib import util
from src import const
from lib import kubejs
from lib import stringCleaning

def deployFunctions():
	for villager in vil.villagers:
		writeSummonCommand(villager)
		writeHighlightCommand(villager)
		if hasTrades(villager):
			writeUpdateTradeCommand(villager)
			writeTradeTooltips(villager)

def writeSummonCommand(villager):
	name = villager[vil.nameKey]
	mcfunction.writeFunction(
		'fc_villagers',
		name,
		easyNpc.summonNpcCommand(
			villager[vil.textureKey],
			name,
			getVillagerOffers(villager)
		)
	)

def writeHighlightCommand(villager):
	name = villager[vil.nameKey]
	mcfunction.writeFunction(
		'fc_villagers',
		f'{name}_highlight',
		easyNpc.highlightNpcCommand(name)
	)

def writeUpdateTradeCommand(villager):
	name = villager[vil.nameKey]
	mcfunction.writeFunction(
		'fc_villagers',
		f'{name}_update_trades',
		easyNpc.updateNpcCommand(
			name,
			getVillagerOffers(villager)
		)
	)

def writeTradeTooltips(villager):
	name = villager[vil.nameKey]
	tooltipContent = tradeTooltipsContent(villager)

	if len(tooltipContent) > 0:
		kubejs.writeClientFile(
			kubejs.tooltipFileContent(tooltipContent),
			f'fc_villager_trades_tooltips_{stringCleaning.cleanedNameStr(name)}'
		)

def tradeTooltipsContent(villager, tradesKey=vil.tradesKey, postScript=''):
	buyFromVillager = []
	sellToVillager = []
	getFromVillager = []
	for offer in getVillagerOffers(villager, tradesKey=tradesKey):
		if offer[easyNpc.playerGiveKey] == const.priceItem:
			buyFromVillager.append(offer[easyNpc.villagerItemsKey])
		elif offer[easyNpc.villagerItemsKey] == const.priceItem:
			sellToVillager.append(offer[easyNpc.playerGiveKey])
		else:
			getFromVillager.append(offer[easyNpc.villagerItemsKey])

	name = villager[vil.nameKey]
	tooltipContent = ""
	if len(buyFromVillager) > 0:
		tooltipContent += kubejs.eventAdd(
			buyFromVillager,
			[f'You can buy this item from {name}{postScript}']
		)
	if len(sellToVillager) > 0:
		tooltipContent += kubejs.eventAdd(
			sellToVillager,
			[f'You can sell this item to {name}{postScript}']
		)
	if len(getFromVillager) > 0:
		tooltipContent += kubejs.eventAdd(
			getFromVillager,
			[f'You can get this item from {name}{postScript}']
		)
	return tooltipContent

def getVillagerOffers(villager, tradesKey=vil.tradesKey):
	if hasTrades(villager):
		offers = []
		for smartTrade in villager[tradesKey]:
			villagerGiveItems = util.defaultDict(
				smartTrade,
				vil.villagerItems,
				[const.priceItem]
			)
			playerGiveItems = util.defaultDict(
				smartTrade,
				vil.playerItems,
				[const.priceItem]
			)
			for villagerGiveItem in villagerGiveItems:
				for playerGiveItem in playerGiveItems:
					offers.append({
						easyNpc.villagerItemsKey: villagerGiveItem,
						easyNpc.villagerQtyKey: util.defaultDict(
							smartTrade,
							vil.villagerNum,
							1
						),
						easyNpc.playerGiveKey: playerGiveItem,
						easyNpc.playerQtyKey: util.defaultDict(
							smartTrade,
							vil.playerNum,
							1
						)
					})
		return offers
	else:
		return []

def hasTrades(villager):
	return vil.tradesKey in villager
