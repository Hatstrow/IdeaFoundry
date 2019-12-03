# Complete project details at https://RandomNerdTutorials.com
import time,
import LightShow as ls

LightShow = ls.LightShow(0,4,5)#initiate lightshow class with pin GPIO 0,4, and 5

print('in main')
HOST = '192.168.1.10'
PORT = 1235
while True:
  try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST,PORT))
    msg = s.recv(8)
    if len(msg) <=0:#continue/start at top of loop if no message
      continue
  except:
    continue
  if str(msg) == 'False': # trying to be able to get out of this loop if message sent == False and "break" the loop
    break
    #if message >0 loop will reach this point and do stuff dependent on whats in the message

  print(msg.decode('utf-8'))
  if str(msg) == "1":
    LightShow.GoodGuys1()
  elif str(msg) == "2":
    LightShow.BadGuys1()
  else
    continue
  
  


