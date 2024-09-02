from input import collectionQuestsInput as cqi
from lib import kubejs
from lib import stringCleaning
from lib import translation
import json

translationKeyParent = 'collectionTooltips'

def genCollectionTooltips():
	translation.removeTranslationsFromJson(translationKeyParent)
	writeTooltips()

def writeTooltips():
	tooltipContent = ''
	for questlineIdx, questline in enumerate(cqi.questlines):
		questLineName = questline[cqi.nameKey]
		if questline[cqi.typeKey] == cqi.itemQuestTypeConst:
			for questGroup in questline[cqi.questGroupsKey]:
				translation.addTranslationsToJson(
					transKey(questLineName),
					stringCleaning.cleanQuotes(questLineName)
				)
				translation.addTranslationsToJson(
					transKey(questGroup[cqi.nameKey]),
					stringCleaning.cleanQuotes(questGroup[cqi.nameKey])
				)

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