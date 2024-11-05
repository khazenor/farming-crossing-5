from input import fishingWeights
import math
from lib import craftingTableSell
from lib import fcTrans

maxFishPrice = 5

transParent = 'fishCraftingTableSell'

def generateFishCraftingSellRecipes():
	fcTrans.setDefaultTranslationParent(transParent)
	fishPrices = getFishPrices()

	craftingTableSell.generateCraftingSellRecipes(
		fishPrices,
		2,
		'fish',
		'es'
	)
	fcTrans.resetDefaultTranslationParent()

def getFishPrices():
	fishWeights = fishingWeights.weights
	highestWeight = 0

	for fish in fishWeights:
		highestWeight = max(highestWeight, fishWeights[fish])

	fishPrices = {}
	for fish in fishWeights:
		fishPrices[fish] = price(fishWeights[fish], highestWeight)
	return fishPrices

def price(fishWeight, highestWeight):
	return math.ceil(
		float(highestWeight - fishWeight) * maxFishPrice / float(highestWeight) + 0.5
	)
