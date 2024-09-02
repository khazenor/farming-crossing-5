from quests import const as qConst
from lib import ftbQuest
from src import const
import os

def replaceInitScoresId():
	questFile = os.path.join(const.ftbChapters(), 'farming_crossing.snbt')
	newQuestFileContent = ''
	keyLineSubstring = 'command: "/function fc_collection:init_all_scores"'
	replaceLine = '					id: "xxidxx"'
	countToReplace = 3
	with open(questFile, 'r') as f:
		oldQuestFileContent = f.read()
	doCount = False
	count = 0
	for line in oldQuestFileContent.split('\n'):
		if keyLineSubstring in line:
			doCount = True
		if doCount:
			count += 1
		if count == countToReplace:
			newQuestFileContent += replaceLine.replace('xxidxx', ftbQuest.randomId(qConst.rewardSeedStarter))
			doCount = False
			count = 0
		else:
			newQuestFileContent += line
		newQuestFileContent += '\n'
	with open(questFile, 'w') as f:
		f.write(newQuestFileContent)


