from lib import stringCleaning

def collectionTally(objName):
	return f"scoreboard players add @p {objName} 1\n"

def collectionNotification(collectedText, objName, total):
	return tellRaw([
		textJson(f'{collectedText} ('),
		scoreJson(objName),
		textJson(f'/{total})'),
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
	outStr = f'scoreboard objectives add {objName} dummy {textJson(title)}\n'
	outStr += f'scoreboard players set @p {objName} 0\n'
	return outStr

def textJson(text):
	return f'{{"text":"{text}"}}'

def textJsonEscaped(text):
	return textJson(text).replace('"', '\\"')

def summonEntity(entityType, entityData=""):
	return f'summon {entityType} ~ ~ ~ {entityData}'
