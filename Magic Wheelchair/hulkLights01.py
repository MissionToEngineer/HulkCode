import RPi.GPIO as GPIO
import subprocess
import time
import random
from neopixel import *
rainbowtoggle = True
chasetoggle = False
sleeptime = .25
def colorWipe(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)
        
def purpleFlash(strip):
    for i in range(0, 5):
        purple = False
        if purple == False:
            for j in range(0, LED_COUNT):
                strip.setPixelColor(j, Color(0, 200, 255))
            strip.show()
            purple = True
            time.sleep(sleeptime)
        if purple == True:
            for a in range(0, LED_COUNT):
                strip.setPixelColor(a, Color(175, 0, 0))
            strip.show()
            time.sleep(sleeptime)
    colorWipe(strip, Color(0,0,0))

def purpleAdvance(strip):
    for i in range(0, LED_COUNT):
        strip.setPixelColor(i, Color(0, 200, 255))
        strip.show()
        time.sleep(sleeptime)
    colorWipe(strip, Color(0,0,0))

def angry(strip):
    for i in range(0, 5):
        red = False
        if red == False:
            for j in range(0, LED_COUNT):
                strip.setPixelColor(j, Color(0, 200, 0))
            strip.show()
            red = True
            time.sleep(sleeptime)
        if red == True:
            for a in range(0, LED_COUNT):
                strip.setPixelColor(a, Color(0, 0, 0))
            strip.show()
            time.sleep(sleeptime)
    colorWipe(strip, Color(0,0,0))

def flashG(strip):
    for i in range(0, 5):
        green = False
        if green == False:
            for j in range(0, LED_COUNT):
                strip.setPixelColor(j, Color(175, 0, 0))
            strip.show()
            green = True
            time.sleep(sleeptime)
        if green == True:
            for a in range(0, LED_COUNT):
                strip.setPixelColor(a, Color(0, 0, 0))
            strip.show()
            time.sleep(sleeptime)
    colorWipe(strip, Color(0,0,0))
            
def flashP(strip):
    for i in range(0, 5):
        purple = False
        if purple == False:
            for j in range(0, LED_COUNT):
                strip.setPixelColor(j, Color(0, 200, 255))
            strip.show()
            purple = True
            time.sleep(sleeptime)
        if purple == True:
            for a in range(0, LED_COUNT):
                strip.setPixelColor(a, Color(0, 0, 0))
            strip.show()
            time.sleep(sleeptime)
    colorWipe(strip, Color(0,0,0))

# LED strip configuration:
LED_COUNT      = 30     # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000     # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 175     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53



# Create NeoPixel object with appropriate configuration.
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
# Intialize the library (must be called once before other functions).
strip.begin()

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(18, GPIO.OUT)
randy = random.randint(0, 5)
print (randy)
if (randy == 0):
    purpleFlash(strip)
if (randy == 1):
    purpleAdvance(strip)
if (randy == 2):
    angry(strip)
if (randy == 3):
    flashG(strip)
if (randy == 4):
    flashP(strip)