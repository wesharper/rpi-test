from gpiozero import DigitalInputDevice
from time import sleep

device: DigitalInputDevice = DigitalInputDevice('BOARD18', pull_up=None)

while True:
    print(device.value)
    sleep(1)