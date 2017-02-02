# CRUMBS
A robust, simple and easy to use GPS data logger. And basic software tools to
perform sanity checks on the collected data.

The first goal of the project is to create ~20 "stage 2" devices that
are ready for use in April 2017.


# Use cases

Potential use cases are infinite, this is a shorter list where we
know of a potential user:

* backup GPS logger for a motorbike based survey of rural areas
* real time fleet tracking by text message


# ROADMAP

This roadmap is organized into stages of development, leading towards
a field tested design that can be extended for new needs.

## Stage 1
* [ ] breadboard assembly of components
* [ ] record GPS traces in memory and SD card
  - [ ] ... using battery power
* [ ] first iteration of a case to house components
* [ ] tools to overlay traces on existing maps

## Stage 2
* [ ] record GPS traces for short time (~2min) and then sleep for a
      long time (10min)
* [ ] second iteration of case
* [ ] combined power supply using 12V motorbike power and a battery

## Stage 3
* [ ] broadcast recorded GPS points when near a friendly WiFi AP
* [ ] server that receives GPS points, can display them and export to other
      formats

## Stage 4
* [ ] add GSM module to transmit location every N minutes
* [ ] server that listens for text messages and records them


# Contributing
CRUMBS is an open project, anyone is welcome to contribute. To propose changes
to any of the documents or software fork this repository and make a Pull
Request. Discuss ideas by creating an issue.


# Licensing
The default license is BSD-3. This is usually applied to software, so do we need
to pick a hardware license that fits the BSD-3 philosophy?
