import os
import ftb_snbt_lib

questTransFolder = '..\\..\\config\\ftbquests\\quests\\lang'

def questTransFileDir(minecraftTransCode):
	return os.path.join(questTransFolder, minecraftTransCode + ".snbt")

def hasTrans(transKey, minecraftTransCode):
	return transKey in dict(loadSnbt(minecraftTransCode)).keys()

def addTrans(transKey, transText, minecraftTransCode):
	snbt = loadSnbt(minecraftTransCode)
	snbt[transKey] = transText
	dumpSnbt(snbt, minecraftTransCode)

def loadSnbt(minecraftTransCode):
	fileLoc = questTransFileDir(minecraftTransCode)
	if os.path.exists(fileLoc):
		return ftb_snbt_lib.load(
			open(fileLoc, 'r', encoding='utf-8')
		)
	else:
		return loadEmptySnbt()

def dumpSnbt(snbt, minecraftTransCode):
	ftb_snbt_lib.dump(
		snbt,
		open(questTransFileDir(minecraftTransCode), "w", encoding='utf-8')
	)

def loadEmptySnbt():
	enSnbt = ftb_snbt_lib.load(
		open(questTransFileDir('en_us'), 'r', encoding='utf-8')
	)
	for key in list(enSnbt.keys()):
		del enSnbt[key]
	return enSnbt
