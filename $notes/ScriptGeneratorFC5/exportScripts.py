from src import marketShopGen
from src import fishCraftingTableSell
from src import floraDuplication
from src import furnitureCutting
from src import customVillagers
from src import musicDiscs

if __name__ == "__main__":
	musicDiscs.deployMusicDiscs()
	customVillagers.deployFunctions()
	furnitureCutting.genFurnitureCuttingSupport()
	floraDuplication.generateDuplicationRecipes()
	fishCraftingTableSell.generateFishCraftingSellRecipes()
	marketShopGen.generateMarketShops()
