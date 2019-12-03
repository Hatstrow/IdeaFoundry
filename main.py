# Complete project details at https://RandomNerdTutorials.com
import time
import TrafficTest
for i in range(4):
    led.value(0)
    time.sleep(1)
    print('led:' + str(i))
    led.value(1)

print('in main')
HOST = '192.168.1.10'
PORT = 1235
while True:
  try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST,PORT))
    msg = s.recv(8)
    if len(msg) <=0:
      continue
  except:
    continue
  if msg == 'False':
    break
  print(msg.decode('utf-8'))
  TrafficTest.all(0,4,5)
  # for i in range(10):
  #   led.value(0)
  #   led2.value(0)
  #   time.sleep(1)
  #   print('led:' + str(i))
  #   led.value(1)
  #   led2.value(1)
  #   time.sleep(1)


