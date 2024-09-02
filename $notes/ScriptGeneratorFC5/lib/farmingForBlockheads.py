from input import marketShop
from src import const
import os
import json

defaultPrice = 1
defaultPriceItem = 'kubejs:miles_ticket'
defaultProductNum = 1

def genCategoryStores(categoriesData):
	for categoryKey in categoriesData:
		categoryData = categoriesData[categoryKey]
		writeCategoryStore(
			categoryKey,
			categoryData[marketShop.nameKey],
			categoryData[marketShop.iconKey],
			categoryData[marketShop.entryGroupsKey]
		)

def writeCategoryStore(categoryKey, name, icon, entryGroups):
	json.dump(
		categoryStore(
			entryGroupsToEntries(entryGroups, categoryKey),
			categoryKey,
			name,
			icon
		),
		open(
			os.path.join(const.farmingForBlockheads(), f"{categoryKey}.json"),
			'w'
		),
		indent=2
	)

def writeCategoryStoreWithEntries(categoryKey, name, icon, entries):
	json.dump(
		categoryStore(entries, categoryKey, name, icon),
		open(
			os.path.join(const.farmingForBlockheads(), f"{categoryKey}.json"),
			'w'
		),
		indent=2
	)

def categoryStore(entries, category, categoryName, categoryItem):
	return {
		"customCategories": {
			category: {
				"name": categoryName,
				"icon": {
					"item": categoryItem
				}
			}
		},
		"customEntries": entries
	}

def entryGroupsToEntries(entryGroups, categoryKey):
	entryList = []
	for entryGroup in entryGroups:
		entryList += entryGroupToEntries(entryGroup, categoryKey)
	return entryList

def entryGroupToEntries(entryGroup, categoryKey):
	entryList = []
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
			entryList.append(entryNBT(
				productId,
				productNum,
				priceItem,
				price,
				categoryKey,
				entryGroup[nbtKey]
			))
		else:
			entryList.append(entry(
				productId,
				productNum,
				priceItem,
				price,
				categoryKey
			))
	return entryList

def entry(item, itemCount, payment, paymentCount, category):
	return {
		"output": { "item": item, "count": itemCount },
		"payment": { "item": payment, "count": paymentCount },
		"category": category
	}

def entryNBT(item, itemCount, payment, paymentCount, category, itemNBT):
	return {
		"output": { "item": item, "count": itemCount, 'nbt': itemNBT},
		"payment": { "item": payment, "count": paymentCount },
		"category": category
	}