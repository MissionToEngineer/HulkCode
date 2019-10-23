import RPi.GPIO as GPIO
import subprocess
import time
import threading

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(36, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
time.sleep(10)
def motors():
    rc = subprocess.call("python pwm.py")

def lights():
    rc = subprocess.call("sh /home/pi/Documents/runLights01.sh", shell=True)

def sound():
    rc = subprocess.call("/home/pi/Documents/randomNumbersArkin.sh", shell=True)
#bb = subprocess.call("sh /home/pi/Documents/connectspeaker.sh", shell=True)

while True:
    time.sleep(.25)
    if (GPIO.input(36) == True):
        x = threading.Thread(target=lights)
        x.start()
        z = threading.Thread(target=sound)
        z.start()
        
        time.sleep(4)
        print ("I schleep")
        sz = subprocess.call("/home/pi/Documents/pwm.py")
        time.sleep(1)
        print ("done schleep")
        x.join()

