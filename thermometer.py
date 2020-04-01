from gpiozero import SmoothedInputDevice
from time import sleep

thermometer: SmoothedInputDevice = SmoothedInputDevice('BOARD18', sample_wait=.5)

while True:
    print(thermometer.is_active)
    print(thermometer.value)
    sleep(.5)