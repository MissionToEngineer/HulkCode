#!/usr/bin/env python
import RPi.GPIO as GPIO
from time import sleep

ledpin = 32
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(ledpin,GPIO.OUT)
pi_pwm = GPIO.PWM(ledpin, 500)
pi_pwm.start(50)
for i in range (0, 6):
    pi_pwm.ChangeDutyCycle(99)#60 for low 97 for high
    sleep(0.01)
    pi_pwm.ChangeDutyCycle(0)
    sleep(0.08)
sleep(1)
for i in range (0, 6):
    pi_pwm.ChangeDutyCycle(60)#60 for low 97 for high
    sleep(0.01)
    pi_pwm.ChangeDutyCycle(0)
    sleep(0.04)
