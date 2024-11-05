from src import const
from lib import questTrans
from lib import fcTrans
import os
from lib import util
from lib import translationApi
from lib import transCache

def main():
	updateFcTranslation()
	updateQuestTranslation()

def updateFcTranslation():
	engFCTrans = fcTrans.loadTransDict()
	langCache = transCache.loadLangCache()
	for transFilename in os.listdir(const.fcTransFolder):
		if const.engLangCode not in transFilename:
			transCode = transFilename.split('.')[0]
			transDict = fcTrans.loadTransDict(transCode)

			for transKey in engFCTrans:
				addToLangCache(engFCTrans[transKey], transDict[transKey], transCode, langCache)
	transCache.dumpLangCache(langCache)

def updateQuestTranslation():
	engQuestTrans = questTrans.loadSnbt()
	langCache = transCache.loadLangCache()
	for transFilename in os.listdir(const.questTransFolder):
		if const.engLangCode not in transFilename:
			transCode = transFilename.split('.')[0]
			transDict = questTrans.loadSnbt(transCode)

			for transKey in engQuestTrans:
				engComponent = engQuestTrans[transKey]
				transComponent = transDict[transKey]
				if type(engComponent) == list:
					for i in range(len(engComponent)):
						addToLangCache(engComponent[i], transComponent[i], transCode, langCache)
				else:
					addToLangCache(engComponent, transComponent, transCode, langCache)
	transCache.dumpLangCache(langCache)

def addToLangCache(engText, transText, transCode, langCache):
	if engText != transText and translationApi.shouldTranslate(engText):
		if engText not in langCache:
			langCache[engText] = {}
		langCache[engText][transCode] = transText
