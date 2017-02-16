# Servers

Collection of servers that can function as REST end point for the
boards.

## simple.py
A small flask webserver that provides an end point to which you can
post data, as well as a "dashboard" where it displays a plot of temperature
and humidity measurements posted by a board. Works well with
`board/temperature-logger.py` as firmware. Remember to adjust the
wifi settings to suit your wifi.
