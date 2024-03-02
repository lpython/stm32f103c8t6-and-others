# https://www.youtube.com/watch?v=zqKJ-f4Iyas&t=315s

import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__),'..')) # this is done for the AMG88xx folder (you may have to rewrite this to include the path of your AMG file)
from time import sleep
import numpy as np
import cv2
import os
os.environ['BLINKA_FT232H'] = "1"
import busio
import board
import adafruit_amg88xx
from pyftdi.ftdi import Ftdi
Ftdi().open_from_url('ftdi:///?')
Ftdi().open_from_url('ftdi://ftdi:232h:1/1')

i2c = busio.I2C(board.SCL, board.SDA)

sensor = adafruit_amg88xx.AMG88XX(i2c)
# wait for AMG to boot
sleep(0.1)
# preallocating variables
norm_pix = []

try:
    while(1):
        norm_pix = np.array(sensor.pixels, dtype = np.uint8)
        im_color = np.zeros((8,8), dtype = np.uint8)
        print(norm_pix)
        cv2.normalize(norm_pix, im_color, 0, 255, cv2.NORM_MINMAX)
        print(im_color)

        im_color = cv2.applyColorMap(im_color, cv2.COLORMAP_JET)

        norm_pix = cv2.resize(im_color, (512,512))

        cv2.imshow("Thermal", norm_pix)
        k = cv2.waitKey(1)
        if k == 27:  # Esc key to stop
                break

except KeyboardInterrupt:
    print("CTRL-C: Program Stopping via Keyboard Interrupt...")

finally:
    print("Exiting Loop")