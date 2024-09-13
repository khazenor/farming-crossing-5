from lib import commands

villagerItemsKey = 'villagerItemsKey'
villagerQtyKey = 'villagerQtyKey'
playerGiveKey = 'playerGiveKey'
playerQtyKey = 'playerQtyKey'

def summonNpcCommand(skinUUID, name, offers):
	with open('input\\villagerTemplate.txt', 'r') as f:
		entityData = f.read()
		entityData = entityData.replace('<<<<customName>>>>', f'"{commands.textJsonEscaped(name)}"')
		entityData = entityData.replace('<<<<offerString>>>>', offerString(offers))
		entityData = entityData.replace('<<<<skinUuid>>>>', skinUUID)
		entityData = entityData.replace('  ', '')
		entityData = entityData.replace('\n', '')
		entityData = entityData.replace(',', ', ')
	return commands.summonEntity('easy_npc:humanoid', entityData=entityData)

def updateNpcCommand(name, offers):
	command = f'data modify entity {nameSelector(name)} Offers set value {offerString(offers)}\n'
	return command

def highlightNpcCommand(name):
	command = 'execute at @p'
	command += f' if entity {nameSelector(name)}'
	command += f' run effect give {nameSelector(name)}'
	command += ' minecraft:glowing 30 1 true'
	command += '\n'
	return command

def nameSelector(name):
	return f'@e[type=easy_npc:humanoid, name={name}, sort=nearest, limit=1]'

def offerString(offers):
	return f"{{Recipes: [{offerRecipeString(offers)}]}}"

# offer: {villagerItems, villagerQty, playerGive, playerQty}
def offerRecipeString(offers):
	offerRecipeStringOut = ""
	for i, offer in enumerate(offers):
		offerRecipeStringOut += '{'
		offerRecipeStringOut += f'buy: {{id: "{offer[playerGiveKey]}", Count: {offer[playerQtyKey]}}}'
		offerRecipeStringOut += f',sell: {{id: "{offer[villagerItemsKey]}", Count: {offer[villagerQtyKey]}}}'
		offerRecipeStringOut += ',maxUses: 2147483647, xp: 0, uses: 0, priceMultiplier: 0.0, specialPrice: 0'
		offerRecipeStringOut += ', demand: 0, rewardExp: 0'
		offerRecipeStringOut += '}'
		if i < len(offers) - 1:
			offerRecipeStringOut += ', '
	return offerRecipeStringOut
