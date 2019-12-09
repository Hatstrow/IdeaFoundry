try:
  import usocket as socket
except:
  import socket

#from machine import Pin
import network, time
import webrepl

import esp
esp.osdebug(None)

import gc
gc.collect()

ssid = 'HouseOfStone 2.4'
password = 'houseofstone12'

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())
webrepl.start()
#led = Pin(5, Pin.OUT)
#led2= Pin(2, Pin.OUT)