from lib import kubejs
from lib import translation
from src import const
from src import questCollectionReader
import os

craftOutputNumber = 8
paymentItem = "minecraft:bone_meal"
floraDenyList = [
	"minecraft:apple",
	"minecraft:bamboo",
	"minecraft:beetroot_seeds",
	"minecraft:brown_mushroom",
	"minecraft:cactus",
	"minecraft:carrot",
	"minecraft:cocoa_beans",
	"minecraft:glow_berries",
	"minecraft:kelp",
	"minecraft:melon_slice",
	"minecraft:potato",
	"minecraft:pumpkin_seeds",
	"minecraft:pumpkin",
	"minecraft:red_mushroom",
	"minecraft:sugar_cane",
	"minecraft:sweet_berries",
	"minecraft:wheat_seeds",
	"farmersdelight:cabbage_seeds",
	"farmersdelight:onion",
	"farmersdelight:rice",
	"farmersdelight:tomato_seeds"
]
transParent = 'floraDuplicationTooltips'

def generateDuplicationRecipes():
	shapelessRecipeContent = ""
	craftedFlora = []

	for flora in questCollectionReader.collectionQuestLineItems('flora_compendium'):
		if flora not in floraDenyList:
			craftedFlora.append(flora)
			shapelessRecipeContent += kubejs.shapeless(flora, [flora, paymentItem], craftOutputNumber)

	with open(os.path.join(const.serverScripts(), 'flora_duplication_crafting.js'), 'w') as f:
		f.write(kubejs.recipeFileContent(shapelessRecipeContent))

	translation.setDefaultTranslationParent(transParent)
	with open(os.path.join(const.clientScripts(), 'flora_duplication_tooltips.js'), 'w') as tooltipFile:
		tooltipFile.write(kubejs.tooltipFileContent(kubejs.eventAddTranslatedTooltips(craftedFlora, [
			"You can craft more of this flora with bone meal"
		])))
	translation.resetDefaultTranslationParent()
