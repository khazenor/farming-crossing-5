import os
def invertDict(parentToChild):
	childToParent = {}
	for parent in parentToChild:
		child = parentToChild[parent]
		if isinstance(child, list):
			addItems = child
		else:
			addItems = [child]

		for addItem in addItems:
			if addItem in childToParent.keys():
				childToParent[addItem].append(parent)
			else:
				childToParent[addItem] = [parent]
	return childToParent

def addToDictList(dictList, key, value):
	if key in dictList.keys():
		dictList[key].append(value)
	else:
		dictList[key] = [value]

def addToDictString(dictString, key, strValue):
	strLine = f'{strValue}\n'
	if key in dictString:
		dictString[key] += strLine
	else:
		dictString[key] = strLine

def appendToSetList(setList, item):
	if item not in setList:
		setList.append(item)

def stringHasSubstringFromList(testString, substrings):
	for substring in substrings:
		if substring in testString:
			return True
	return False

def defaultDict(dictVar, tryKey, default):
	if tryKey in dictVar:
		return dictVar[tryKey]
	else:
		return default

def removeFiles(folder):
	if os.path.exists(folder):
		for filename in os.listdir(folder):
			os.remove(os.path.join(folder, filename))
