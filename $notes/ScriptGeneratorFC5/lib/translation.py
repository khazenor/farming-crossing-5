import json
from lib import stringCleaning
from src import const
import os

langCode = 'en_us'
defaultTranslationParent = 'defaultTranslationParent'
defaultTranslationParentCopy = defaultTranslationParent

def resetLangCode():
	global langCode
	langCode = 'en_us'
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

def transExists(transKey):
	return dictHasTrans(loadTransDict(), transKey)

def dumpTransDict(transDict):
	json.dump(
		transDict,
		open(const.modpackTransFileDir(langCode), 'w', encoding='utf-8'),
		indent=2,
		sort_keys=True,
		ensure_ascii=False
	)

def loadTransDict():
	transFileLoc = const.modpackTransFileDir(langCode)
	if os.path.exists(transFileLoc):
		return json.load(open(transFileLoc, 'r', encoding='utf-8'))
	else:
		return {}

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
