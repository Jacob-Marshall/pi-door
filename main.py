# Inport modules
from gpiozero import Button
from time import sleep
from datetime import datetime

door = Button(26)
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
door_open = false

print("It's working!")

while True:
    if door.is_pressed:
        door_open = true
        print("Your door was opened at" current_time)
    sleep(100)
    
