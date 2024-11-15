from src import const
from lib import questTrans
from lib import fcTrans
import os
from lib import transCache

def main():
	updateFcTranslation()
	updateQuestTranslation()

def updateFcTranslation():
	engFCTrans = fcTrans.loadTransDict()
	for transFilename in os.listdir(const.fcTransFolder):
		if const.engLangCode not in transFilename:
			transCode = transFilename.split('.')[0]
			transDict = fcTrans.loadTransDict(transCode)

			for transKey in engFCTrans:
				if transKey in transDict:
					transCache.addToLangCache(engFCTrans[transKey], transDict[transKey], transCode)

def updateQuestTranslation():
	engQuestTrans = questTrans.loadSnbt()
	for transFilename in os.listdir(const.questTransFolder):
		if const.engLangCode not in transFilename:
			transCode = transFilename.split('.')[0]
			transDict = questTrans.loadSnbt(transCode)

			for transKey in engQuestTrans:
				engComponent = engQuestTrans[transKey]
				if transKey in transDict:
					transComponent = transDict[transKey]
					if type(engComponent) == list:
						for i in range(len(engComponent)):
							transCache.addToLangCache(engComponent[i], transComponent[i], transCode)
					else:
						transCache.addToLangCache(engComponent, transComponent, transCode)

def removeUnusedTranslationFromCache(engTextsUsedByModpack):
	transCacheDict = transCache.loadLangCache()
	transCacheKeys = list(transCacheDict.keys())
	for transCacheKey in transCacheKeys:
		if transCacheKey not in engTextsUsedByModpack:
			del transCacheDict[transCacheKey]
	transCache.dumpLangCache(transCacheDict)
