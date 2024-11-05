import re

def shouldTranslate(engText):
	engHasText = bool(re.search('[a-zA-Z]', engText))
	if not engHasText:
		return False
	else:
		return True
