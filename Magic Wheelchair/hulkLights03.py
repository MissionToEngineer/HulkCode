import RPi.GPIO as GPIO
import subprocess
import time
from neopixel import *
rainbowtoggle = True
chasetoggle = False

def angry(strip):
    for i in range(0, 5):
        red = False
        if red == False:
            for j in range(0, LED_COUNT):
                strip.setPixelColor(j, Color(0, 200, 0))
            strip.show()
            red = True
            time.sleep(1)
        if red == True:
            for a in range(0, LED_COUNT):
                strip.setPixelColor(a, Color(0, 0, 0))
            strip.show()
            time.sleep(1)

# LED strip configuration:
LED_COUNT      = 27     # Number of LED pixels.
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
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(18, GPIO.OUT)
GPIO.output(18, 0)
while True:
    angry(strip)

