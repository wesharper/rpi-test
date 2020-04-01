from gpiozero import DigitalInputDevice
from time import sleep

thermometer: DigitalInputDevice = DigitalInputDevice('BOARD18')

while True:
    print(thermometer.value)
    sleep(1)