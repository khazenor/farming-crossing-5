from input import marketShop
from src import const
import os
import json
from lib import translation
from lib import util
from lib import datapacks
from lib import stringCleaning
import shutil

defaultPrice = 1
defaultPriceItem = 'kubejs:miles_ticket'
defaultProductNum = 1

datapackName = 'Farming For Blockheads Market Integration'
dataFolder = datapacks.dataFolder(const.fcDataPacksFolder(), datapackName)
categoryFolder = f'{dataFolder}\\farmingforblockheads\\market_categories'
entriesFolder = f'{dataFolder}\\farmingforblockheads\\recipe\\market\\farming_crossing'
presetRoot = 'farming_crossing'
presetsFolder = f'{dataFolder}\\{presetRoot}\\market_presets'
transKeyParent = 'farmingForBlockheads.market'

def genMarket(categoriesData):
	datapacks.remakeDataPack(const.fcDataPacksFolder(), datapackName)
	util.makeFolders([ categoryFolder, entriesFolder, presetsFolder])
	translation.removeTranslationsFromJson(transKeyParent)
	genCategoryStores(categoriesData)

def genCategoryStores(categoriesData):
	for i in range(len(categoriesData.keys())):
		categoryKey = list(categoriesData.keys())[i]
		categoryData = categoriesData[categoryKey]
		writeCategoryStore(
			categoryKey,
			categoryData[marketShop.nameKey],
			categoryData[marketShop.iconKey],
			categoryData[marketShop.entryGroupsKey],
			i
		)

def writeCategoryStore(categoryKey, name, icon, entryGroups, sortIdx):
	writeCategoryFile(name, icon, categoryKey, sortIdx)
	writeEntryGroupsEntries(entryGroups, categoryKey)

def writeCategoryFile(name, icon, categoryKey, sortIdx):
	transKey = translation.tKey(transKeyParent, name)
	translation.addTranslationsToJson(transKey, name)

	json.dump(
		{
			"tooltip": {
				"translate": transKey
			},
			"icon": {
				"id": icon
			},
			"sortIndex": sortIdx
		},
		open(os.path.join(categoryFolder, f"{categoryKey}.json"), 'w'),
		indent=2
	)

def writeEntryGroupsEntries(entryGroups, categoryKey):
	for entryGroup in entryGroups:
		writeEntryGroupToEntries(entryGroup, categoryKey)

def writeEntryGroupToEntries(entryGroup, categoryKey):
	for productId in entryGroup[marketShop.itemsKey]:
		priceKey = marketShop.priceKey
		productNumKey = marketShop.productNumKey
		priceItemKey = marketShop.priceItemKey
		nbtKey = marketShop.nbtKey
		if priceKey in entryGroup:
			price = entryGroup[priceKey]
		else:
			price = defaultPrice
		if priceItemKey in entryGroup:
			priceItem = entryGroup[priceItemKey]
		else:
			priceItem = defaultPriceItem
		if productNumKey in entryGroup:
			productNum = entryGroup[productNumKey]
		else:
			productNum = defaultProductNum

		if nbtKey in entryGroup:
			nbt = entryGroup[nbtKey]
		else:
			nbt = None
		writeEntry(
			productId,
			productNum,
			priceItem,
			price,
			categoryKey,
			nbt=nbt
		)

def writeEntry(item, itemCount, payment, paymentCount, category, nbt=None):
	writePreset(payment, paymentCount)
	writeMarketRecipe(category, presetName(payment, paymentCount), item, itemCount,nbt=nbt)

def writePreset(paymentId, paymentCount):
	presetFile = os.path.join(presetsFolder, presetName(paymentId, paymentCount))+'.json'
	if not os.path.exists(presetFile):
		json.dump(
			{
				"enabled": True,
				"payment": {
					"ingredient": {
						"item": paymentId
					},
					"count": paymentCount
				}
			},
			open(presetFile, 'w'),
			indent=2
		)

def writeMarketRecipe(category, presetName, item, itemCount, nbt=None):
	result = {
		"count": itemCount,
		"item": item
	}
	if nbt is not None:
		result["nbt"] = nbt
	json.dump(
		{
			"type": "farmingforblockheads:market",
			"category": f"farmingforblockheads:{category}",
			"preset": f"{presetRoot}:{presetName}",
			"result": {
				"count": itemCount,
				"item": item
			}
		},
		open(os.path.join(entriesFolder, cleanedDomainName(category, item))+'.json', 'w'),
		indent=2
	)


def presetName(paymentId, paymentCount):
	return cleanedDomainName(paymentId, paymentCount)

def cleanedDomainName(domain, name):
	return f"{stringCleaning.cleanedNameStr(domain)}_{stringCleaning.cleanedNameStr(name)}"
def entryNBT(item, itemCount, payment, paymentCount, category, itemNBT):
	return {
		"output": { "item": item, "count": itemCount, 'nbt': itemNBT},
		"payment": { "item": payment, "count": paymentCount },
		"category": category
	}