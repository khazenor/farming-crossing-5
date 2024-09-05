from list import furnitureCutting as fList
from input import woodFurnitureInput as wIn
from lib import util
from lib import kubejs
from lib import translation

def genFurnitureCuttingSupport():
	woodAndContent, woodAndFurniture, allCuttables, materials = sortThroughData()

	kubejs.generateSimpleTags(allCuttables, 'forge:furniture_cuttable', 'furniture_all_cuttable_tags')
	genCuttingRecipes(woodAndContent)
	genTooltips(woodAndFurniture, materials)

def genCuttingRecipes(woodAndContent):
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
			# recipeContent += kubejs.woodcutting(tag, singleFurniture, 1)
	kubejs.writeServerFile(
		kubejs.recipeFileContent(
			recipeContent
		),
		'furniture_cutting_recipes'
	)
	kubejs.writeServerFile(
		kubejs.tagsContent(
			tagContent
		),
		'furniture_cutting_tags'
	)

def genTooltips(woodAndFurniture, materials):
	translation.setDefaultTranslationParent('furnitureCuttingTooltips')
	tooltipContent = kubejs.eventAddTranslatedTooltips(
		materials,
		[
			"Put this block into a Stonecutter",
			"to make different furniture"
		]
	)
	for wood in woodAndFurniture:
		tooltipContent += kubejs.eventAddTranslatedTooltips(
			woodAndFurniture[wood],
			[
				f"You can make this furniture by putting",
				f"{wood.replace('_', ' ')} in to a Stonecutter"
			]
		)
	kubejs.writeClientFile(
		kubejs.tooltipFileContent(
			tooltipContent
		),
		'furniture_cutting_tooltips'
	)
	translation.resetDefaultTranslationParent()


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
