from deep_translator import GoogleTranslator
from src import const
from lib import translation
import json

languages = {
	"zh_tw": "zh-TW"
}

def translateTexts():
	en_us = json.load(open(const.translationModpackLoc, 'r'))
	for minecraftLangCode in languages:
		translation.langCode = minecraftLangCode
		translator = GoogleTranslator(source='auto', target=languages[minecraftLangCode])
		for transKey in en_us:
			if not translation.transExists(transKey):
				engText = en_us[transKey]
				transText = translator.translate(engText)
				translation.addTranslationsToJson(transKey, transText)