"""Simple firmware for a temperature logger"""
from dht import DHT22
import machine
import network
import time

import urequests


# turn off the access point
ap_if = network.WLAN(network.AP_IF)
ap_if.active(False)

# join existing hotspot
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect("G2_8802", "manchester")

while not sta_if.isconnected():
    time.sleep(0.5)

print('network config:', sta_if.ifconfig())

led = machine.Pin(0, machine.Pin.OUT)
led.high()

dht_pin = machine.Pin(4)
dht = DHT22(dht_pin)

observations = []

N = 0

while True:
    time.sleep(5)

    led.low()
    time.sleep(0.05)
    led.high()

    dht.measure()
    t = time.time()
    payload = {'time': t,
               'temp': dht.temperature(),
               'humidity': dht.humidity(),
               }
    observations.append(payload)
    print('observing', payload)

    if N%4 == 0 and sta_if.isconnected():
        while observations:
            payload = observations[-1]
            try:
                time.sleep(0.5)
                r = urequests.post("http://192.168.43.87:5000/sensor",
                                   json=payload)
                r.close()
                print('sent', payload)

            except Exception as e:
                print(e)
                break
            _ = observations.pop()

    N += 1
