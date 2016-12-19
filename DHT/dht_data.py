#!/usr/bin/python3
#Import lib
import Adafruit_DHT
import sys
import time
import csv

# Def temps 
DA = time.strftime("%Y-%m-%d")
HE = time.strftime("%H:%M:%S")

# type de sonde.
sensor_args = { '11': Adafruit_DHT.DHT11,
                '22': Adafruit_DHT.DHT22,
                '2302': Adafruit_DHT.AM2302 }
if len(sys.argv) == 3 and sys.argv[1] in sensor_args:
  sensor = sensor_args[sys.argv[1]]
  pin = sys.argv[2]
else:
    print('usage: sudo python3 dht_data.py [11|22|2302] GPIOpin')
    print('example: sudo python3 dht_data.py 22 4 - lire sonde dht22 sur le GPIO #4')


#def val
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
humidity = round(humidity, 2)
temperature = round(temperature, 2)

if humidity is not None and temperature is not None:
  print ('Temp = {0:0.1f}*C  HumD = {1:0.1f}%'.format(temperature, humidity))
else:
  print ('Pas de sonde!')

data = [DA, HE, humidity, temperature]
# export vers /my/path/
csvfile = "/home/pi/DATAPIN4_" + DA + ".csv"

#ajout valeur & delimiteur.
with open(csvfile, "a") as output:
  writer = csv.writer(output, delimiter=";", lineterminator='\n')
  writer.writerow(data)
#Dodo
sys.exit(1)
