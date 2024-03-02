# SPDX-FileCopyrightText: 2021 Melissa LeBlanc-Williams for Adafruit Industries
#
# SPDX-License-Identifier: MIT
import time
import board
import busio

spi = busio.SPI(board.SCLK, board.MOSI, board.MISO)
while not spi.try_lock():
    pass
spi.configure(baudrate=1000)
spi.unlock()

def read_from_spi():
    # cs_pin.value = False  # Activate the chip select
    data = bytearray(10)  # Read 4 bytes of data (adjust as needed)
    spi.readinto(data)
    # cs_pin.value = True  # Deactivate the chip select
    return data

while True:
    received_data = read_from_spi()
    print("Received data:", received_data)
    time.sleep(0.1)