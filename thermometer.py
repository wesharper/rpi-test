from gpiozero import DigitalInputDevice
from time import sleep

device: DigitalInputDevice = DigitalInputDevice(5)

while True:
    print(device.value)
    sleep(1)