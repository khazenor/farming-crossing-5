from deep_translator import GoogleTranslator
from src import const
from lib import translation
from lib import questTrans
import json

languages = {
	"zh_tw": "zh-TW"
}

def translateTexts():
	transModpackFeatureTexts()
	transQuests()

def transModpackFeatureTexts():
	en_us = json.load(open(const.fcTransFileDir('en_us'), 'r'))
	for minecraftLangCode in languages:
		translation.langCode = minecraftLangCode
		translator = GoogleTranslator(source='auto', target=languages[minecraftLangCode])
		for transKey in en_us:
			if not translation.transExists(transKey):
				engText = en_us[transKey]
				transText = translator.translate(engText)
				translation.addTranslationsToJson(transKey, transText)

def transQuests():
	en_us = questTrans.loadSnbt('en_us')
	for minecraftLangCode in languages:
		translator = GoogleTranslator(source='auto', target=languages[minecraftLangCode])
		for transKey in en_us:
			if not questTrans.hasTrans(transKey, minecraftLangCode):
				engComponent = en_us[transKey]
				if type(engComponent) == list:
					transList = []
					for engText in engComponent:
						transList.append(translator.translate(engText))
					questTrans.addTrans(transKey, transList, minecraftLangCode)
					pass
				else:
					transText = translator.translate(engComponent)
					questTrans.addTrans(transKey, transText, minecraftLangCode)
					pass


