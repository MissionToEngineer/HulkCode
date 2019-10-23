import RPi.GPIO as GPIO
import subprocess
import time
from neopixel import *
rainbowtoggle = True
chasetoggle = False
def wheel(pos):
    """Generate rainbow colors across 0-255 positions."""
    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)

def colorWipe(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)

def rainbowCycle(strip, wait_ms=20, iterations=5):
    for j in range(256*iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((int(i * 256 / strip.numPixels()) + j) & 255))
        strip.show()
        print("test")
        time.sleep(wait_ms/1000.0)

def theaterChaseRainbow(strip, wait_ms=50):
    """Rainbow movie theater light style chaser animation."""
    for j in range(256):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, wheel((i+j) % 255))
            strip.show()
            time.sleep(wait_ms/1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, 0)

def purpleAdvance(strip):
    for i in range(0, LED_COUNT):
        strip.setPixelColor(i, Color(0, 200, 255))
        strip.show()
        time.sleep(1)

def purpleFlash(strip):
    for i in range(0, 5):
        purple = False
        if purple == False:
            for j in range(0, LED_COUNT):
                strip.setPixelColor(j, Color(0, 200, 255))
            strip.show()
            purple = True
            time.sleep(1)
        if purple == True:
            for a in range(0, LED_COUNT):
                strip.setPixelColor(a, Color(175, 0, 0))
            strip.show()
            time.sleep(1)

def base(strip):
    for i in range(0, LED_COUNT):
        strip.setPixelColor(i, Color(175, 0, 0))
        strip.show()
def greenCrawl(strip)
    for a in range(0, LED_COUNT):
        strip.setPixelColor(a, Color(0, 200, 255))
        strip.show()
    for i in range(0, LED_COUNT):
        strip.setPixelColor(i, Color(175, 0, 0))
        strip.setPixelColor(i+1, Color(175, 0, 0))
        strip.setPixelColor(i+2, Color(175, 0, 0))
        strip.show

# LED strip configuration:
LED_COUNT      = 3     # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
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
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(18, GPIO.OUT)
#GPIO.output(18, 0)
while True:
    #rainbowCycle(strip)
    colorWipe(strip, Color(0, 0, 0))
    if (GPIO.input(16) == GPIO.HIGH):
        colorWipe(strip, Color(255, 255, 255))
        time.sleep(3)

while False:
    if (GPIO.input(10) == GPIO.HIGH):
        rainbowtoggle = not rainbowtoggle
        time.sleep(1)
        GPIO.output(18, 1)
    if (GPIO.input(16) == GPIO.HIGH):
        chasetoggle = not chasetoggle
        time.sleep(1)
        #print("Button was pushed!")
        #rc = subprocess.call("./hulksmash.sh", shell=True)
    try:
        print(chasetoggle, rainbowtoggle)
        rainbowCycle(strip)
        theaterChaseRainbow(strip)
        
    except KeyboardInterrupt:
        colorWipe(strip, Color(0,0,0), 10)
    if rainbowtoggle == False and chasetoggle == False:
        colorWipe(strip, Color(0,0,0), 10)