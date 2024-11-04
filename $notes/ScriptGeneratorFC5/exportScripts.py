from src import marketShopGen
from src import fishCraftingTableSell
from src import floraDuplication
from src import furnitureCutting
from src import customVillagers
from src import translate

if __name__ == "__main__":
	translate.translateTexts()
	customVillagers.deployFunctions()
	furnitureCutting.genFurnitureCuttingSupport()
	furnitureCutting.genGenericCuttingSupport()
	floraDuplication.generateDuplicationRecipes()
	fishCraftingTableSell.generateFishCraftingSellRecipes()
	marketShopGen.generateMarketShops()
