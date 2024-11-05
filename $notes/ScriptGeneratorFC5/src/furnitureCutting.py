from list import furnitureCutting as fList
from input import woodFurnitureInput as wIn
from lib import util
from lib import kubejs
from lib import fcTrans
from input import genericCuttingInput as gIn

def genFurnitureCuttingSupport():
	woodAndContent, woodAndFurniture, allCuttables, materials = sortThroughData()

	kubejs.generateSimpleTags(allCuttables, 'forge:furniture_cuttable', 'furniture_all_cuttable_tags')
	genCuttingRecipes(woodAndContent)
	genTooltips(woodAndFurniture, materials)

def genGenericCuttingSupport():
	cuttingItemDict = gIn.cuttingItemDict
	baseToCuttables = {}
	baseToCuttablesNoBase = {}
	baseNames = list(cuttingItemDict.keys())
	for baseName in cuttingItemDict:
		materialDict = cuttingItemDict[baseName]
		baseToCuttables[baseName] = materialDict[gIn.cuttablesKey]
		baseToCuttables[baseName].append(materialDict[gIn.baseKey])
		baseToCuttablesNoBase[baseName] = materialDict[gIn.cuttablesKey]

	genCuttingRecipes(baseToCuttables, baseName='generic')
	genTooltips(baseToCuttablesNoBase, baseNames, baseName='generic')

def genCuttingRecipes(woodAndContent, baseName="furniture"):
	tagContent = ""
	recipeContent = ""
	for wood in woodAndContent:
		furniture = woodAndContent[wood]
		tag = f"forge:furniture_{wood}"
		tagContent += kubejs.eventAddItemToList(
			tag,
			furniture
		)
		for singleFurniture in furniture:
			recipeContent += kubejs.eventStonecutting(singleFurniture, f"#{tag}")
			recipeContent += kubejs.woodcutting(tag, singleFurniture, 1)
	kubejs.writeServerFile(
		kubejs.recipeFileContent(
			recipeContent
		),
		f'{baseName}_cutting_recipes'
	)
	kubejs.writeServerFile(
		kubejs.tagsContent(
			tagContent
		),
		f'{baseName}_cutting_tags'
	)

def genTooltips(woodAndFurniture, materials, baseName="furniture"):
	fcTrans.setDefaultTranslationParent('furnitureCuttingTooltips')
	tooltipContent = kubejs.eventAddTranslatedTooltips(
		materials,
		[
			"Put this block into a Sawmill or a Stonecutter",
			"to make different furniture"
		]
	)
	for wood in woodAndFurniture:
		tooltipContent += kubejs.eventAddTranslatedTooltips(
			woodAndFurniture[wood],
			[
				f"You can make this furniture by putting",
				f"{wood.replace('_', ' ')} in to a Sawmill or a Stonecutter"
			]
		)
	kubejs.writeClientFile(
		kubejs.tooltipFileContent(
			tooltipContent
		),
		f'{baseName}_cutting_tooltips'
	)
	fcTrans.resetDefaultTranslationParent()


def sortThroughData():
	woodAndContent = {}
	woodAndFurniture = {}
	materials = []
	allCuttables = []
	for furnitureItemId in fList.possibleWoodFurniture:
		wood, initContent = getWoodAndInitContent(furnitureItemId)
		if wood != -1:
			if wood not in woodAndContent:
				woodAndContent[wood] = initContent
				materials += initContent

			woodAndContent[wood].append(furnitureItemId)
			util.addToDictList(woodAndFurniture, wood, furnitureItemId)
			allCuttables.append(furnitureItemId)

	return woodAndContent, woodAndFurniture, allCuttables, materials


def getWoodAndInitContent(itemId):
	isPlank = util.stringHasSubstringFromList(itemId, wIn.planksKeys)
	for woodInfo in wIn.woodTypesInfo:
		if util.stringHasSubstringFromList(itemId, woodInfo[wIn.translationKey]):
			if isPlank:
				return f"{woodInfo[wIn.woodKey]}_planks", woodInfo[wIn.plankContentKey]
			else:
				return f"{woodInfo[wIn.woodKey]}_log", woodInfo[wIn.contentKey]
	return -1, -1
