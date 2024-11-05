from src import const
from lib import fcTrans
from lib import questTrans
from lib import translationApi
from src import updateTransCache
import json

languages = {
	"zh_tw": "zh-TW"
}

def translateTexts():
	updateTransCache.main()
	transModpackFeatureTexts()
	transQuests()

def transModpackFeatureTexts():
	en_us = json.load(open(const.fcTransFileDir(const.engLangCode), 'r'))
	for transCode in languages:
		fcTrans.langCode = transCode
		for transKey in en_us:
			engText = en_us[transKey]
			transText = translationApi.translate(engText, transCode)
			fcTrans.addTranslationsToJson(transKey, transText, transCode)

def transQuests():
	en_us = questTrans.loadSnbt(const.engLangCode)
	for transCode in languages:
		for transKey in en_us:
			engComponent = en_us[transKey]
			if type(engComponent) == list:
				transList = []
				for engText in engComponent:
					transList.append(translationApi.translate(engText, transCode))
				questTrans.addTrans(transKey, transList, transCode)
			else:
				transText = translationApi.translate(engComponent, transCode)
				questTrans.addTrans(transKey, transText, transCode)
