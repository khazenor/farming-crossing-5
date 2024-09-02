from lib import stringCleaning
from lib import translation

transKeyParent = 'mcCommands'
def collectionTally(objName):
	return f"scoreboard players add @p {objName} 1\n"

def collectionNotification(collectedText, objName, total):
	return tellRaw([
		translateJson(f'{collectedText} ('),
		scoreJson(objName),
		translateJson(f'/{total})'),
	])

def tellRaw(texts):
	outStr = 'tellraw @p [""'
	for text in texts:
		outStr += ', '
		outStr += text
	outStr += ']\n'
	return outStr

def scoreJson(objective):
	return f'{{"score":{{"name":"@p","objective":"{objective}"}}}}'

def initScoreBoard(title):
	objName = stringCleaning.cleanedNameStr(title)
	outStr = f'scoreboard objectives add {objName} dummy {translateJson(title)}\n'
	outStr += f'scoreboard players set @p {objName} 0\n'
	return outStr

def translateJson(text):
	transKey = f"{transKeyParent}.{stringCleaning.cleanedNameStr(text)}"
	translation.addTranslationsToJson(transKey, text)

	return f'{{"translate":"{transKey}"}}'

def textJsonEscaped(text):
	return translateJson(text).replace('"', '\\"')

def summonEntity(entityType, entityData=""):
	return f'summon {entityType} ~ ~ ~ {entityData}'
