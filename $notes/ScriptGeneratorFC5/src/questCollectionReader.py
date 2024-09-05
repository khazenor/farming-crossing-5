from input import collectionQuestsInput as cqIn

itemCollectableFiles = ['aquarium', 'flora_compendium', 'mineral_museum']
collectionQuestGroupDenyNames = [
	'Ore Completion'
]
def collectionQuestItems():
	collectableItems = []
	for questline in cqIn.questlines:
		for questGroup in questline[cqIn.questGroupsKey]:
			for task in questGroup[cqIn.tasksKey]:
				if questline[cqIn.filenameKey] in itemCollectableFiles:
					if questGroup[cqIn.nameKey] not in collectionQuestGroupDenyNames:
						collectableItems.append(task)
				elif questline[cqIn.filenameKey] == 'animal_watching':
					collectableItems.append(task[cqIn.iconKey])
	return collectableItems

def collectionQuestLineItems(questLineFileName):
	collectableItems = []
	for questline in cqIn.questlines:
		for questGroup in questline[cqIn.questGroupsKey]:
			for task in questGroup[cqIn.tasksKey]:
				if questline[cqIn.filenameKey] == questLineFileName:\
					collectableItems.append(task)
	return collectableItems


# def questSpawnEggs():
# 	spawnEggs = []
# 	for questline in cqIn.questlines:
# 		if questline[cqIn.filenameKey] == 'animal_watching':
# 			for questGroup in questline[cqIn.questGroupsKey]:
# 				for task in questGroup[cqIn.tasksKey]:
# 					spawnEggs.append(task[cqIn.iconKey])
# 	return spawnEggs
#
# def nonQuestSpawnEggs(allEggs):
# 	nonQuestEggs = []
# 	questSpawnEggsList = questSpawnEggs()
# 	for egg in allEggs:
# 		if egg not in questSpawnEggsList:
# 			nonQuestEggs.append(egg)
# 	return nonQuestEggs
