# Firmware

This directory contains various firmwares for a ESP8266. You should
move each one to your chip and rename it `main.py`.

(If you use `ampy` with python3 put'ing a file seems to not work?)


## temperature-logger.py
Logs temperature and humidity, sends it to a REST end point like
`server/simple.py` when it has connectivity. Otherwise stores the
data in flash memory until it can send it again. Remember to adjust the
wifi settings to suit your wifi. This depends on `urequests.py` so add
it to the flash memory as well.
