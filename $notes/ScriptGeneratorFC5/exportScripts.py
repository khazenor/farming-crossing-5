from src import marketShopGen
from src import fishCraftingTableSell
from src import floraDuplication
from src import furnitureCutting
from src import customVillagers

if __name__ == "__main__":
	customVillagers.deployFunctions()
	furnitureCutting.genFurnitureCuttingSupport()
	floraDuplication.generateDuplicationRecipes()
	fishCraftingTableSell.generateFishCraftingSellRecipes()
	marketShopGen.generateMarketShops()
