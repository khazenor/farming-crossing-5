import re

def cleanedNameStr(nameStr):
	newStr = re.sub('[^a-zA-Z0-9 _]+','', nameStr)
	newStr = re.sub(' +', '_', newStr)
	newStr = newStr.lower()
	return newStr

def cleanQuotes(inStr):
	return inStr.replace("'", "\\'")
