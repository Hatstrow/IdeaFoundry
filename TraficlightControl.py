import requests, datetime, os, machine
from bs4 import BeautifulSoup


class SiteScraper(self):
	'''this will first determine if we have a recent 
	version of the schedule. This will update maybe only once a year. 
	This will help reduce the amount of requests made to the website
	https://www.cbssports.com/college-football/teams/OHIOST/ohio-state-buckeyes/'''

	def Schedule():
		#gets information about the current schedule 
		#to determine if app should be tracking live game data

	def GameDay():
		#determines if today and time is game day

	def FileCreateUpdate():
		#creates or updates txt file with specific information

	def GetScore():
		#gets live score from web


class LightSwitch(self):
	'''this will control what mode the light is in
	Mode 1: Game day lights
	Mode 2: Random light show
	Mode 3: All on'''



class main(self):
	while True:
