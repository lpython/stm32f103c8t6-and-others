import board
import busio
import digitalio
import time

# Create an SPI object
spi = busio.SPI(board.SCK, board.MOSI, board.MISO)

# Initialize a digital pin for chip select (CS/SS)
cs_pin = digitalio.DigitalInOut(board.D10)
cs_pin.direction = digitalio.Direction.OUTPUT

def write_to_spi():
    cs_pin.value = False  # Activate the chip select
    spi.write(bytearray([1]))  # Write a single byte with value 1
    cs_pin.value = True  # Deactivate the chip select

while True:
    write_to_spi()
    print("Wrote '1' to SPI bus")
    time.sleep(1)  # Wait for 1 second
