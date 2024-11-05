import util

cacheFileDir = 'cache\\translationCache.json'

def loadLangCache():
	return util.loadJson(cacheFileDir)

def dumpLangCache(langCache):
	util.dumpJson(langCache, cacheFileDir)