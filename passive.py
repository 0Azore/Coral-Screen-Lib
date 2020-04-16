import math
import time
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont, ImageOps
import adafruit_rgb_display.st7789 as st7789

cs_pin = digitalio.DigitalInOut(board.GPIO_P36)
dc_pin = digitalio.DigitalInOut(board.GPIO_P22)
reset_pin = None
BAUDRATE = 64000000
spi = board.SPI()
disp = st7789.ST7789(spi, cs=cs_pin, dc=dc_pin, rst=reset_pin, baudrate=BAUDRATE, width=135, height=240, x_offset=53, y_offset=40)
 
# Create blank image for drawing.
# Make sure to create image with mode 'RGB' for full color.
height = disp.width   # we swap height/width to rotate it to landscape!
width = disp.height
image = Image.new('RGBA', (width, height))
rotation = 90
 

draw = ImageDraw.Draw(image)

draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
disp.image(image, rotation)

padding = -2
top = padding
bottom = height-padding
x = 0
font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 24)
i = 0
rFreq = 1.66/50
gFreq = 2.66/50
bFreq = 3.66/50
while True:
    i = i + 1
    draw.rectangle((0, 0, width, height), outline=0, fill=(math.floor(255*math.sin(rFreq*i)),math.floor(255*math.sin(gFreq*i)),math.floor(255*math.sin(bFreq*i)),255))
    disp.image(ImageOps.mirror(image),rotation)
    #time.sleep(.1)

