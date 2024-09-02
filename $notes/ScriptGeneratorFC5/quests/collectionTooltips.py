from input import collectionQuestsInput as cqi
from lib import kubejs
from lib import stringCleaning

def genCollectionTooltips():
	tooltipContent = ''
	for questlineIdx, questline in enumerate(cqi.questlines):
		questLineName = questline[cqi.nameKey]
		if questline[cqi.typeKey] == cqi.itemQuestTypeConst:
			for questGroup in questline[cqi.questGroupsKey]:
				tooltipContent += kubejs.eventAdd(
					questGroup[cqi.tasksKey],
					[
						stringCleaning.cleanQuotes(questLineName),
						stringCleaning.cleanQuotes(questGroup[cqi.nameKey])
					]
				)
	kubejs.writeClientFile(
		kubejs.tooltipFileContent(tooltipContent),
		'collection_tooltips'
	)
