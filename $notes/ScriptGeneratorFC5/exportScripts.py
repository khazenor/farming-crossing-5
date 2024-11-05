from src import marketShopGen
from src import fishCraftingTableSell
from src import floraDuplication
from src import furnitureCutting
from src import customVillagers
from src import translateModpackTexts

if __name__ == "__main__":
	translateModpackTexts.translateTexts()
	customVillagers.deployFunctions()
	furnitureCutting.genFurnitureCuttingSupport()
	furnitureCutting.genGenericCuttingSupport()
	floraDuplication.generateDuplicationRecipes()
	fishCraftingTableSell.generateFishCraftingSellRecipes()
	marketShopGen.generateMarketShops()
