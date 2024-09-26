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
	transDict = json.load(open(translationLoc, 'r'))
	transDict[transKey] = text
	dumpTransDict(transDict)

def removeTranslationsFromJson(translationKeyParent):
	transDict = json.load(open(translationLoc, 'r'))
	while dictHasTrans(transDict, translationKeyParent):
		removeATransFromDict(transDict, translationKeyParent)
	dumpTransDict(transDict)

def dumpTransDict(transDict):
	json.dump(transDict, open(translationLoc, 'w'), indent=2, sort_keys=True)

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
	childKey = stringCleaning.cleanedNameStr(text)
	childKey = stringCleaning.toLowerCamelCaseIfSnake(childKey)
	return f"{parentKey}.{childKey}"