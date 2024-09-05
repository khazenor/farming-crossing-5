from src import marketShopGen
from src import fishCraftingTableSell
from src import floraDuplication
from src import furnitureCutting

if __name__ == "__main__":
	furnitureCutting.genFurnitureCuttingSupport()
	floraDuplication.generateDuplicationRecipes()
	fishCraftingTableSell.generateFishCraftingSellRecipes()
	marketShopGen.generateMarketShops()
