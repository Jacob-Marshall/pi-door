#!/usr/bin/python
# -*- coding: utf-8 -*-
# Inport modules

from gpiozero import Button
from time import sleep
from datetime import datetime
import requests

# Variables

door = Button(26)
now = datetime.now()
current_time = now.strftime('%H:%M:%S')
door_open = '\nYour door was opened at', current_time
door_open_time = str(door_open).encode()

# open and read the file after the appending:

f = open('log.txt', 'r')
print f.read()

print "It's working!"

while True:
    if door.is_pressed:
        # File handling
        f = open('log.txt', 'w')
        f = open('log.txt', 'a')
        f.write(door_open_time)
        f.close()
    sleep(1)
