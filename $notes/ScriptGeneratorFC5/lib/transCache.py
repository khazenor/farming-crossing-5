from lib import util

cacheFileDir = 'cache\\translationCache.json'

def hasCachedTrans(engText, transCode):
	langCache = loadLangCache()
	if engText not in langCache:
		return False

	return transCode in langCache[engText]

def getCachedTrans(engText, transCode):
	return loadLangCache()[engText][transCode]

def loadLangCache():
	return util.loadJson(cacheFileDir)

def dumpLangCache(langCache):
	util.dumpJson(langCache, cacheFileDir)