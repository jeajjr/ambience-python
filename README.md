# Ambience python application

## The project

Project page: [Ambience](https://jeajjr.github.io/ambience/)

## Python application

This repository contains the python source code, embedded on an ESP8266 board
running [Micropython](https://docs.micropython.org/en/latest/esp8266/quickref.html).

## Functionality

The application open a TCP server on port 45225. It expects three bytes to be 
received, representing the intensity of the Red, Green and Blue lights, where 0
represents an off-state and 255 a full-intensity state.
