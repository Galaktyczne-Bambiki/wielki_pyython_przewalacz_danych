import serial
import requests
import time
import random

while True:
  with serial.Serial() as ser:
    ser.baudrate = 9600
    ser.port = '/dev/ttyUSB0'
    ser.open()
    try:
      while True:
        data = float(ser.readline())
        # data = 21.37
        url = 'http://130.61.73.118:5000/api/temperature-reports'
        myobj = {
                  "latitude": random.uniform(-180, 180),
                  "longitude": random.uniform(-180,180),
                  "celsiusValue": data
                }
        x = requests.post(url, json = myobj)
        print(myobj)
        print(x)
        time.sleep(1)
    except KeyboardInterrupt:
      ser.close()
      exit()
    except Exception as err:
      print("ERROR: ", err)
      ser.close()