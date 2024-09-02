from input import collectionQuestsInput as cqIn

def questSpawnEggs():
	spawnEggs = []
	for questline in cqIn.questlines:
		if questline[cqIn.filenameKey] == 'animal_watching':
			for questGroup in questline[cqIn.questGroupsKey]:
				for task in questGroup[cqIn.tasksKey]:
					spawnEggs.append(task[cqIn.iconKey])
	return spawnEggs

def nonQuestSpawnEggs(allEggs):
	nonQuestEggs = []
	questSpawnEggsList = questSpawnEggs()
	for egg in allEggs:
		if egg not in questSpawnEggsList:
			nonQuestEggs.append(egg)
	return nonQuestEggs
