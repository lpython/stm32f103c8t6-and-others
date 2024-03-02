import board
import digitalio
import time

import supervisor

# Disable autoreload
supervisor.disable_autoreload()


led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT



while True:
    print("Hello, circuitpython!")
    led.value = True
    time.sleep(0.5)
    led.value = False
    time.sleep(0.5)