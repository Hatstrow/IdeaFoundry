import requests, os
import time as ttim #machine #used with microPy
from bs4 import BeautifulSoup
from datetime import date


class SiteScraper():
	'''this will first determine if we have a recent 
	version of the schedule. This will update maybe only once a year. 
	This will help reduce the amount of requests made to the website
	https://www.cbssports.com/college-football/teams/OHIOST/ohio-state-buckeyes/   https://www.cbssports.com/college-football/teams/OHIOST/ohio-state-buckeyes/schedule/'''
	def __init__(self,url_y,url_c,team,year):
		self.url_cbs = url_c
		self.url_yahoo = url_y
		self.team = team
		self.teamFile = team +'_'+str(date.today().year)+'_TeamData.txt'
		self.time = date.today()
		self.year = year
	
	# def Schedule(self):
	# 	#gets information about the current schedule 
	# 	#to determine if app should be tracking live gasme datas

	# 	if self.teamFile in os.listdir():
	# 		with open(self.teamFile, 'r') as f:
	# 			schedule = f.readlines()
	# 	else:
	# 		schedule = []
			
	# 	if any(str(self.time.year) in i for i in schedule): #compiles the team schedule into the text document as rows and iterate through them
	# 		return schedule
	# 	else:
	# 		ScheduleUrl = self.url +'schedule/'
	# 		# try:
	# 		# 	req = requests.get(ScheduleUrl)
	# 		# except e as error:
	# 		# 	return LightShow.errorDoes(error)
	# 		page = BeautifulSoup(requests.get(ScheduleUrl).content, 'html.parser')
	# 		opponet = [i.text.strip() for i in page.find_all(class_='TeamName')]
	# 		GameTime = [i.text.strip() for i in page.find_all(class_='CellGameDate')]

	# 		with open(self.teamFile, 'a+') as f:
	# 			for i in range(len(opponet)):
	# 				f.write(str(GameTime[i]) + " :" + str(opponet[i]) +'\n')
	# 		with open(self.teamFile, 'r') as f:
	# 			schedule = f.readlines()
	# 	return schedule
	def GameLinks(self):
		Url =self.url_yahoo +'schedule/?season='+self.year
		soup = BeautifulSoup(requests.get(Url).content, 'html.parser')
		Games_yahoo = soup.find_all(class_='Bgc(bg-mod) Bgc(secondary):h Pos(r) H(45px) Cur(p)')
		GameLinks = [i.a['href'] for i in Games_yahoo]
		GameFeild = [i.text[0:5] for i in Games_yahoo]  
		for i in GameFeild:
			if "@" in i:
				i = "@"
			else:
				i = 'Vs'

		return GameLinks, GameFeild 

	def Schedule_Yahoo(self):
		#gets information about the current schedule 
		#to determine if app should be tracking live gasme datas

		if self.teamFile in os.listdir():
			with open(self.teamFile, 'r') as f:
				schedule = f.readlines()	
		else:
			ScheduleUrl_CBS = self.url_cbs +'schedule/'
			soup2_CBS = BeautifulSoup(requests.get(ScheduleUrl_CBS).content, 'html.parser')


			Opponet = [i.text.strip() for i in soup2_CBS.find_all(class_='TeamName')]
			GameTime = [i.text.strip() for i in soup2_CBS.find_all(class_='CellGameDate')]

			links,feild = self.GameLinks()
			print(len(GameTime))
			print(len(feild))
			print(len(links))
			print(len(Opponet))

			with open(self.teamFile, 'a+') as f:
				for i in range(len(Opponet)):
					f.write(str(GameTime[i]) + " :" + str(Opponet[i]) + '  '+ feild[i] + '   ' + links[i] + '\n')

			with open(self.teamFile, 'r') as f:
				schedule = f.readlines()

		return schedule


	def IsGameDay(self):
		#determines if today and time is game day
		print("todays date is: " + self.time.strftime('%b %#d, %Y'))
		index = 0
		for i in self.Schedule_Yahoo():
			#if any(str(self.time.strftime('%b %#d, %Y')) in i for i in schedule): #add '#' in strftime to eliminate leading 0
			if str(self.time.strftime('%b %#d, %Y')) in i:
				print('Game Day!!!!')

				return True, index
			else:
				index +=1
		print('Not a game day')
		return False, index

	def GetScore(self):
		#gets live score from web
		#I can check the "live" web site if its showing actual live results instead of checking 
		#the the team website for for the live link, I would/could check for if times are the same
		#use Yahoo! https://sports.yahoo.com/nfl/minnesota-vikings-dallas-cowboys-20191110006/
		tf,index = self.IsGameDay()
		if tf == True:
			link,feild = self.GameLinks()
			gametime =""
			cycle = 0
			urlLink = 'https://sports.yahoo.com//' + str(link[index])
			print(link[index])
			if feild == "@":
				scoreAttr = ""
			else:
				scoreAttr = ""
			while gametime != 'Final' or cycles<10800:#at 5sec/cycle would be about 15 hours
				score = BeautifulSoup(requests.get(urlLink).content,'lxml')
				cycle+=1
				print(cycle)
				print(score.find_all(class_='Fw(500)')[4].text)
				ttim.sleep(5)
			
		else:
			return 0

		pass

class LightShow():
		
	'''
		this has the diffrent light shows that will be activiated 
		dependent on light switch mode and specical modes for during game day
		jjjj
	'''	

	def __init__(self):
		
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


	def ErrorCodes(self,code):
		self.code = code

		if self.code == 404:
			'''blink diffrent flasshes for code
			ex FFFF  FFFF        FFFF  FFFF
				4  0  4
			'''
			pass 
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


x = SiteScraper('https://sports.yahoo.com/ncaaf/teams/ohio-st/','https://www.cbssports.com/college-football/teams/OHIOST/ohio-state-buckeyes/','ohio-st','2019')
#https://www.cbssports.com/college-football/teams/OHIOST/ohio-state-buckeyes/
#https://www.cbssports.com/nfl/teams/GB/green-bay-packers/schedule/
x.Schedule_Yahoo()

print(x.IsGameDay())
x.GetScore()