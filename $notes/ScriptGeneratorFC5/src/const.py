import os

priceItem = "kubejs:miles_ticket"

def serverScripts():
	return os.path.join(kubejs(), 'server_scripts', 'auto_generated')

def clientScripts():
	return os.path.join(kubejs(), 'client_scripts', 'auto_generated')

def startupScripts():
	return os.path.join(kubejs(), 'startup_scripts', 'auto_generated')

def bountifulPools():
	return os.path.join(data(), "bountiful", "bounty_pools", "bountiful")
def farmersDelightCooking():
	return os.path.join(farmersDelightRecipes(), 'cooking')

def farmersDelightRecipes():
	return os.path.join(farmersDelight(), "recipes")

def farmersDelight():
	return os.path.join(data(), 'farmersdelight')

def data():
	return os.path.join(kubejs(), 'data')

def assets():
	return os.path.join(kubejs(), 'assets')

def farmingForBlockheads():
	return os.path.join(data(), 'farmingforblockheads', 'farmingforblockheads_compat')

def kubejs():
	return '..\\..\\kubejs'

def fcDataPacksFolder():
	return '..\\..\\global_packs\\fc_datapacks'

def config():
	return '../../config'

def ftbquests():
	return os.path.join(config(), "ftbquests")

def ftbChapters():
	return os.path.join(ftbquests(), "quests", "chapters")