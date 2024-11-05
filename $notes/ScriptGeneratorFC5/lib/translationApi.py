import re
from deep_translator import GoogleTranslator
from lib import transCache

languages = {
	"zh_tw": "zh-TW",
	"ko_kr": "ko"
}

def translate(engText, transCode):
	if not shouldTranslate(engText):
		return engText
	if transCache.hasCachedTrans(engText, transCode):
		return transCache.getCachedTrans(engText, transCode)

	translator = GoogleTranslator(source='auto', target=languages[transCode])
	translatedText = translator.translate(engText)
	transCache.addToLangCache(engText, translatedText, transCode)
	return translatedText

def shouldTranslate(engText):
	filteredEngText = engText.replace('%s', '')
	engHasText = bool(re.search('[a-zA-Z]', filteredEngText))
	if not engHasText:
		return False
	else:
		return True
