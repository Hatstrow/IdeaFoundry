import requests, os #machine #used with microPy
from bs4 import BeautifulSoup
from datetime import date


class SiteScraper():
	'''this will first determine if we have a recent 
	version of the schedule. This will update maybe only once a year. 
	This will help reduce the amount of requests made to the website
	https://www.cbssports.com/college-football/teams/OHIOST/ohio-state-buckeyes/   https://www.cbssports.com/college-football/teams/OHIOST/ohio-state-buckeyes/schedule/'''
	def __init__(self,url,team):
		self.url = url
		self.team = team
		self.teamFile = team + 'TeamData.txt'
		self.time = date.today()
	
	def Schedule(self):
		#gets information about the current schedule 
		#to determine if app should be tracking live gasme datas
		if self.teamFile in os.listdir():
			with open(self.teamFile, 'r') as f:
				schedule = f.readlines()
		else:
			schedule = []
			
		if self.time.year in schedule: #self.time:# today: I would like to compile the team schedule into the text document as rows and iterate through them
		#this way I can determine if today is a gameday without even having to make a request
			return schedule
		else:
			ScheduleUrl = self.url +'schedule/'
			page = BeautifulSoup(requests.get(ScheduleUrl).content, 'html.parser')
			opponet = [i.text.strip() for i in page.find_all(class_='TeamName')]
			GameTime = [i.text.strip() for i in page.find_all(class_='CellGameDate')]

			with open(self.teamFile, 'a+') as f:
				for i in range(len(opponet)):
					f.write(str(GameTime[i]) + ":" + str(opponet[i]) +'\n')
			with open(self.teamFile, 'r') as f:
				schedule = f.readlines()

		return schedule
		

	def IsGameDay(self):
		#determines if today and time is game day
		schedule = self.Schedule()
		print (self.time.strftime('%b %d, %Y'))
		if self.time.strftime('%b %d, %Y') in schedule:
			print('Game Day!!!!')
			return True
		else:
			print('Not a game day')
			return False

	def GetScore():
		#gets live score from web
		pass

def LightSwitchMode(input):
	'''this will control what mode the light is in
	Mode 1: Game day lights
	Mode 2: Random light show
	Mode 3: All on'''
	if input == 1: # this is just temp code until I figure out how I want to program this
		return True
	elif input == 2:
		return True
	else:
		return True
	return False

	

	

class LightShow:
	'''
	this has the diffrent light shows that will be activiated 
	dependent on light switch mode and specical modes for during game day
	'''

	def __init__(self):
		pass

	def AllOn(self):
		pass

	def funLightShow_1(self):
		pass

	def funLightShow_2(self):
		pass

	def funLightShow_3(self):
		pass	

	def GameLightShow_1(self):
		pass

	def GameLightShow_2(self):
		pass

	def GameLightShow_3(self):
		pass











class main():
	while True:
		break
	pass


x = SiteScraper('https://www.cbssports.com/nfl/teams/GB/green-bay-packers/','GBP')
#https://www.cbssports.com/college-football/teams/OHIOST/ohio-state-buckeyes/
#https://www.cbssports.com/nfl/teams/GB/green-bay-packers/schedule/
x.Schedule()

print(x.IsGameDay())