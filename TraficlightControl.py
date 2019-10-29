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
		self.time = date.today()
	
	def Schedule(self):
		#gets information about the current schedule 
		#to determine if app should be tracking live game data
		#f = open('teamData.txt', 'r')
		text = 'x'#f.read().split()
		#f.close()


		if text == 'x':# today:
			return True
		else:
			ScheduleUrl = self.url +'schedule/'
			page = BeautifulSoup(requests.get(ScheduleUrl).content, 'html.parser')
			return Flase

		return ScheduleUrl
		

	def GameDay():
		#determines if today and time is game day
		pass

	def FileCreateUpdate():
		#creates or updates txt file with specific information
		pass

	def GetScore():
		#gets live score from web
		pass
	pass

class LightSwitch:
	'''this will control what mode the light is in
	Mode 1: Game day lights
	Mode 2: Random light show
	Mode 3: All on'''
	pass



class main():
	while True:
		break
	pass


x = SiteScraper('https://www.cbssports.com/college-football/teams/OHIOST/ohio-state-buckeyes/','OSU')
print(x.Schedule())