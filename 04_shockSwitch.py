#!/usr/bin/env python3
import RPi.GPIO as GPIO

ShockPin = 11
LedPin = 12

Led_status = 1


def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(LedPin, GPIO.OUT)
    GPIO.setup(ShockPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.output(LedPin, GPIO.HIGH)


def swLed(ev=None):
    global Led_status
    Led_status = not Led_status
    GPIO.output(LedPin, Led_status)
    print("led: " + ("on" if Led_status else "off"))


def loop():
    GPIO.add_event_detect(ShockPin, GPIO.FALLING, callback=swLed, bouncetime=200)
    while True:
        pass


def destroy():
    GPIO.output(LedPin, GPIO.LOW)
    GPIO.cleanup()


if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
