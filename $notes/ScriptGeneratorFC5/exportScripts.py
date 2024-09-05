from src import marketShopGen
from src import fishCraftingTableSell
from src import floraDuplication

if __name__ == "__main__":
	floraDuplication.generateDuplicationRecipes()
	fishCraftingTableSell.generateFishCraftingSellRecipes()
	marketShopGen.generateMarketShops()
