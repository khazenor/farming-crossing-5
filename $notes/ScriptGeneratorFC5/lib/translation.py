import json
from lib import stringCleaning

translationLoc = '..\\..\\global_packs\\fc_packs\\modpack_translations\\assets\\farming_crossing\\lang\\en_us.json'
defaultTranslationParent = 'defaultTranslationParent'
defaultTranslationParentCopy = defaultTranslationParent

def setDefaultTranslationParent(newParent):
	global defaultTranslationParent
	defaultTranslationParent = newParent
	removeTranslationsFromJson(newParent)

def resetDefaultTranslationParent():
	global defaultTranslationParent
	global defaultTranslationParentCopy
	defaultTranslationParent = defaultTranslationParentCopy

# returns transKey
def addDefaultTransToJson(text):
	transKey = tKey(defaultTranslationParent, text)
	addTranslationsToJson(transKey, text)
	return transKey

def addTranslationsToJson(transKey, text):
	transDict = loadTransDict()
	transDict[transKey] = text
	dumpTransDict(transDict)

def removeTranslationsFromJson(translationKeyParent):
	transDict = loadTransDict()
	while dictHasTrans(transDict, translationKeyParent):
		removeATransFromDict(transDict, translationKeyParent)
	dumpTransDict(transDict)

def dumpTransDict(transDict):
	json.dump(transDict, open(translationLoc, 'w'), indent=2, sort_keys=True)

def loadTransDict():
	return json.load(open(translationLoc, 'r'))

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

def tKey(parentKey, text):
	transDict = loadTransDict()
	if text in transDict.values():
		for transKey in transDict:
			if transDict[transKey] == text and parentKey in transKey:
				return transKey

	childKey = stringCleaning.cleanedNameStr(text)
	childKey = stringCleaning.toLowerCamelCaseIfSnake(childKey)
	transKey = f"{parentKey}.{childKey}"
	if transKey in transDict:
		i = 0
		while f"{transKey}{i}" in transDict:
			i += 1
		transKey = f"{transKey}{i}"
	return transKey
