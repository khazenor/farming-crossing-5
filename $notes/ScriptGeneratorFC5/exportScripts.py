from src import marketShopGen
from src import fishCraftingTableSell
from src import floraDuplication
from src import furnitureCutting
from src import customVillagers
from src import translateModpackTexts
from src import updateTransCache

if __name__ == "__main__":
	updateTransCache.main()
	# translateModpackTexts.translateTexts()
	customVillagers.deployFunctions()
	furnitureCutting.genFurnitureCuttingSupport()
	furnitureCutting.genGenericCuttingSupport()
	floraDuplication.generateDuplicationRecipes()
	fishCraftingTableSell.generateFishCraftingSellRecipes()
	marketShopGen.generateMarketShops()
