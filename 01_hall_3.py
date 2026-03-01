#!/usr/bin/env python3
import time

import ADC0832
import RPi.GPIO as GPIO

"""
Example showing hall-sensor digital and analog outputs.
While the loop prints analog values, a GPIO interrupt waits for changes
on the digital output pin.
"""

# Digital out of sensor connected to pin 16 (BOARD layout)
HALL = 16


GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(HALL, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def change_detected(channel):
    print("Change detected")


def init():
    ADC0832.setup()


GPIO.add_event_detect(HALL, GPIO.BOTH, change_detected, bouncetime=25)


def loop():
    while True:
        res0 = ADC0832.getResult(0)
        res1 = ADC0832.getResult(1)
        print(f"res0 = {res0}, res1 = {res1}")
        time.sleep(0.2)


if __name__ == '__main__':
    init()
    try:
        loop()
    except KeyboardInterrupt:
        ADC0832.destroy()
