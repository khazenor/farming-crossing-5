import json

translationLoc = '..\\..\\kubejs\\assets\\kubejs\\lang\\en_us.json'

def addTranslationsToJson(transKey, text):
	transDict = json.load(open(translationLoc, 'r'))
	transDict[transKey] = text
	json.dump(transDict, open(translationLoc, 'w'), indent=2)

def removeTranslationsFromJson(translationKeyParent):
	transDict = json.load(open(translationLoc, 'r'))
	while dictHasTrans(transDict, translationKeyParent):
		removeATransFromDict(transDict, translationKeyParent)

def removeATransFromDict(transDict, translationKeyParent):
	for transKey in transDict:
		if translationKeyParent in transKey:
			del transDict[transKey]
			return

def dictHasTrans(transDict, translationKeyParent):
	for transKey in transDict:
		if translationKeyParent in transKey:
			return True
	return False