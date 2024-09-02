from input import collectionQuestsInput as cqi
from lib import kubejs
from lib import stringCleaning
import json

translationLoc = '..\\..\\kubejs\\assets\\kubejs\\lang\\en_us.json'
translationKeyParent = 'collectionTooltips'

def genCollectionTooltips():
	removeTranslationsFromJson()
	addTranslationsToJson()
	writeTooltipKubeJsFile()

def removeTranslationsFromJson():
	transDict = json.load(open(translationLoc, 'r'))
	while dictHasTrans(transDict):
		removeATransFromDict(transDict)

def removeATransFromDict(transDict):
	for transKey in transDict:
		if translationKeyParent in transKey:
			del transDict[transKey]
			return

def dictHasTrans(transDict):
	for transKey in transDict:
		if translationKeyParent in transKey:
			return True
	return False
def addTranslationsToJson():
	transDict = json.load(open(translationLoc, 'r'))
	for questlineIdx, questline in enumerate(cqi.questlines):
		questLineName = questline[cqi.nameKey]
		if questline[cqi.typeKey] == cqi.itemQuestTypeConst:
			for questGroup in questline[cqi.questGroupsKey]:
				transDict[transKey(questLineName)] = stringCleaning.cleanQuotes(questLineName)
				transDict[transKey(questGroup[cqi.nameKey])] = stringCleaning.cleanQuotes(questGroup[cqi.nameKey])
	json.dump(transDict, open(translationLoc, 'w'), indent=2)

def writeTooltipKubeJsFile():
	tooltipContent = ''
	for questlineIdx, questline in enumerate(cqi.questlines):
		questLineName = questline[cqi.nameKey]
		if questline[cqi.typeKey] == cqi.itemQuestTypeConst:
			for questGroup in questline[cqi.questGroupsKey]:
				tooltipContent += kubejs.eventAdd(
					questGroup[cqi.tasksKey],
					[
						kubejs.transStr(transKey(questLineName)),
						kubejs.transStr(transKey(questGroup[cqi.nameKey]))
					],
					doQuoteOutput=False
				)
	kubejs.writeClientFile(
		kubejs.tooltipFileContent(tooltipContent),
		'collection_tooltips'
	)

def transKey(str):
	return f"{translationKeyParent}.{stringCleaning.cleanedNameStr(str)}"