import requests, os, socket
import time as ttim #machine #used with microPy
from bs4 import BeautifulSoup
from datetime import date


class SiteScraper():
	'''this will first determine if we have a recent 
	version of the schedule. This will update maybe only once a year. 
	This will help reduce the amount of requests made to the website
	https://www.cbssports.com/college-football/teams/OHIOST/ohio-state-buckeyes/   https://www.cbssports.com/college-football/teams/OHIOST/ohio-state-buckeyes/schedule/'''
	def __init__(self,team,year,ipAdress, PORT):
		self.url_cbs = 'https://www.cbssports.com/college-football/teams/OHIOST/ohio-state-buckeyes/'
		self.url_yahoo = 'https://sports.yahoo.com/ncaaf/teams/ohio-st/schedule/?season='
		self.team = team
		self.teamFile = team +'_'+str(date.today().year)+'_TeamData.txt'
		self.time = date.today()
		self.year = year
		self.ipAdress = ipAdress
		self.PORT = PORT
	
	def GameLinks(self):
		'''
		Gets the link to the live web page of the game on Yahoo sports
		'''
		Url =self.url_yahoo+self.year
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

			with open(self.teamFile, 'a+') as f:
				for i in range(len(Opponet)):
					f.write(str(GameTime[i]) + " :" + str(Opponet[i]) + '  '+ feild[i] + '   ' + links[i] + '\n')

			#with open(self.teamFile, 'r') as f: # this wasn't nessesary as I can just generate the info from the file. This would save memeory I think
				#schedule = f.readlines()

		return True #schedule

	def IsGameDay(self):
		#determines if today and time is game day
		print("todays date is: " + self.time.strftime('%b %#d, %Y'))
		index = 0
		#for i in self.Schedule_Yahoo():
		for i in open(self.teamFile, 'r'): 
			#if any(str(self.time.strftime('%b %#d, %Y')) in i for i in schedule): #add '#' in strftime to eliminate leading 0
			if str(self.time.strftime('%b %#d, %Y')) in i:
				return True, index
			else:
				index +=1
		return False, index

	def PushScore(self, WhoScore):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.bind((self.ipAdress,1235))
		s.listen(5)
		
		clientsocket, address = s.accept()
		clientsocket.send(bytes(str(WhoScore), 'utf-8'))
		clientsocket.close()


	def GetScore(self):
		#gets live score from web
		#I can check the "live" web site if its showing actual live results instead of checking 
		#the the team website for for the live link, I would/could check for if times are the same
		#use Yahoo! https://sports.yahoo.com/nfl/minnesota-vikings-dallas-cowboys-20191110006/
		ifTrue,index = self.IsGameDay()
		if ifTrue == True:
			print("Its Game Day Baby!!!!")
		else:
			print('Sorry, Not Game Day :(')
		if ifTrue == True:
			link,feild = self.GameLinks()
			gametime =""
			cycle = 0
			goodguys = ''
			badguys = '0'
			urlLink = 'https://sports.yahoo.com/' + str(link[index])
			print(link[index])
			#GameBar = BeautifulSoup(urlLink,'lxml').find_all(class_='scrollingContainer')[1]# this contains the live game ribbon
			if '@' in feild[index]:
				ggScoreAttr = "Fz(48px) D(b) My(0px) Lh(56px) Or(3) Fw(500) Ta(end) Px(10px)" #good team
				bgScoreAttr = "Fz(48px) D(b) My(0px) Lh(56px) Or(3) Fw(500) Ta(start) Px(10px)"#home team
				print('away')
			else:
				bgScoreAttr = "Fz(48px) D(b) My(0px) Lh(56px) Or(3) Fw(500) Ta(end) Px(10px)" #bad team
				ggScoreAttr = "Fz(48px) D(b) My(0px) Lh(56px) Or(3) Fw(500) Ta(start) Px(10px)" #good team
				print('home')
			score = BeautifulSoup(requests.get(urlLink).content,'lxml')

			while gametime != 'Final' or cycles<10800 or gametime == False:#at 5sec/cycle would be about 15 hours
				score = BeautifulSoup(requests.get(urlLink).content,'lxml')
				cycle+=1
				print(cycle)
				try:
					ggNewScore = score.find_all(class_='scrollingContainer')[1].find_all(class_=ggScoreAttr)[0].text
					bgNewScore = score.find_all(class_='scrollingContainer')[1].find_all(class_=bgScoreAttr)[0].text
				except:
					print("half-Time or game hasn't started") 
					ttim .sleep(20)
					continue
				ttim.sleep(20)
				print('----------------')
				print('before if')
				print(ggNewScore)
				print(goodguys)
				print(badguys)
				print(bgNewScore)
				if ggNewScore > goodguys:
					goodguys = ggNewScore
					self.PushScore('1')
					print('SCORE!!!')
					
					
				if bgNewScore > badguys or goodguys< ggNewScore:
					goodguys = ggNewScore
					badguys = bgNewScore
					self.PushScore('2')
					print('BAD SCORE :( ')
				print('after if')
				print(goodguys)
				print(ggNewScore)
				print(badguys)
				print(bgNewScore)
				print('-------------------')
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



if __name__ == '__main__':
	x = SiteScraper('ohio-st','2019','192.168.1.10', 1234) #socket.gethostname())
	#https://www.cbssports.com/college-football/teams/OHIOST/ohio-state-buckeyes/
	#https://www.cbssports.com/nfl/teams/GB/green-bay-packers/schedule/
	x.Schedule_Yahoo()

	print(x.IsGameDay())
	x.GetScore()













#__________________________________________________________
#|---------------------------------------------------------|
#|this is old code, I want to hang onto incase I need it   |
#|_________________________________________________________|



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