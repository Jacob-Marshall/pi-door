# Inport modules
from gpiozero import Button
from time import sleep

door = Button(2)

while True:
    if door.is_pressed:
        print("Open")
    else:
        print("Closed")
    sleep(1)
