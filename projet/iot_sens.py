from lcd1602 import LCD1602
from machine import Pin, ADC, I2C
from utime import sleep
from dht11 import *
import network
import socket
import struct
import time

degree =[
    0b01100, 
    0b10010,
    0b10010,
    0b01100, 
    0b00000, 
    0b00000, 
    0b00000, 
    0b00000,]

ssid = 'electroProjectWifi'
password = 'M13#MRSE'
NTP_DELTA = 2208988800
host = "pool.ntp.org"

i2c = I2C(1,scl = Pin(7), sda = Pin(6),freq = 400000)
d = LCD1602(i2c,2,16)
ls = ADC(0)
dht = DHT(18)

d.create_char(0,degree)
d.display()

#connecting to wifi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)
d.clear()
d.print('connection')
i=0
while wlan.isconnected() == False:
    d.setCursor(i,1)
    d.print('.')
    if i < 16:
        i=i+1
    else:
        i = 0
        d.clear()
        d.print('connection')
    sleep(1)
ip = wlan.ifconfig()[0]
d.clear()
d.print('Connected on')
d.setCursor(0,1)
d.print(ip)

sleep(1)
#set time from NTP
NTP_QUERY = bytearray(48)
NTP_QUERY[0] = 0x1B
addr = socket.getaddrinfo(host, 123)[0][-1]
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    s.settimeout(1)
    res = s.sendto(NTP_QUERY, addr)
    msg = s.recv(48)
finally:
    s.close()
#print(msg)
val = struct.unpack("!I", msg[40:44])[0]
t = val - NTP_DELTA    
tm = time.gmtime(t)
machine.RTC().datetime((tm[0], tm[1], tm[2], tm[6] + 1, tm[3], tm[4], tm[5], 0))

while True:
    (year, month, day, weekday, hours, minutes, seconds, subseconds) = machine.RTC().datetime()
    (temp, humidity) = dht.readTempHumid()
    d.clear()
    d.setCursor(0,0)
    d.print('H:'+"%03d"%humidity)
    
    d.setCursor(6,0)
    d.print("%02d"%day+'/'+"%02d"%month+'/'+"%02d"%year)
    
    d.setCursor(0,1)
    d.print('T:'+"%03d"%temp)
    d.write(0)
    d.print('C')
    
    d.setCursor(8,1)
    d.print("%02d"%hours+':'+"%02d"%minutes+':'+"%02d"%seconds)
    
    brns = ls.read_u16()
    print(brns/256)
    
    sleep(1)

