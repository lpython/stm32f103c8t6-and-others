# https://www.youtube.com/watch?v=zqKJ-f4Iyas&t=315s

import sys
import os.path
# sys.path.append(os.path.join(os.path.dirname(__file__),'..')) # this is done for the AMG88xx folder (you may have to rewrite this to include the path of your AMG file)
from time import sleep
# import numpy as np
# import cv2
import os
os.environ['BLINKA_FT232H'] = "1"
import busio
import board
import digitalio
# import adafruit_amg88xx
from pyftdi.ftdi import Ftdi
# Ftdi().open_from_url('ftdi:///?')
Ftdi().open_from_url('ftdi://ftdi:232h:1/1')

spi = busio.SPI(board.SCLK, board.MOSI, board.MISO)
while not spi.try_lock():
    pass
spi.configure(baudrate=24e6)
spi.unlock()

cs_pin = digitalio.DigitalInOut(board.D7)
cs_pin.direction = digitalio.Direction.OUTPUT
cs_pin.value = True

out_buf, in_buf = bytearray(1), bytearray(1)

counter = 0

try:
    while(1):
        out_buf[0] = counter
        while not spi.try_lock():
            pass
        cs_pin.value = False
        spi.write_readinto(out_buf, in_buf)
        cs_pin.value = True
        spi.unlock()

        print("Recieved: ", in_buf)

        sleep(0.3)
        counter += 1



except KeyboardInterrupt:
    print("CTRL-C: Program Stopping via Keyboard Interrupt...")

finally:
    print("Exiting Loop")