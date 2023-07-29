from adafruit_hid.mouse import Mouse
import time
import random
import neopixel
import usb_hid
import board


DELAY = 1
TRIGGER_TIME = 5 * 60
mouse = Mouse(usb_hid.devices)
pixel = neopixel.NeoPixel(board.NEOPIXEL, 1)

def colorwheel(pos):
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    if pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    pos -= 170
    return (pos * 3, 0, 255 - pos * 3)

def jiggle_mouse():
    pixel.fill((0,255,0))
    pos = 0
    timer_count = 0
    cont = True
    while cont:
        pixel.fill(colorwheel(pos))
        pos += 1
        pos = pos % 255
        if timer_count == TRIGGER_TIME or timer_count == 0:
            for i in range(0,3):
                x_or_y = random.randint(0, 1)
                if x_or_y == 1:
                    mouse.move(x=random.randint(-400, 400))
                else:
                    mouse.move(y=random.randint(-400, 400))
                time.sleep(DELAY*2)
            timer_count = 0
        timer_count += 1
        time.sleep(DELAY)