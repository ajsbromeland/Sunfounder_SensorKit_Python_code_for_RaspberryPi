#!/usr/bin/env python3
"""
ADC0832 helper for SunFounder sensor kit examples.

Wiring (BOARD numbering):
    CS  -> pin 11
    CLK -> pin 12
    DIO -> pin 13
"""

import time

import RPi.GPIO as GPIO

ADC_CS = 11
ADC_CLK = 12
ADC_DIO = 13


# Using default pins for backwards compatibility.
def setup(cs=11, clk=12, dio=13):
    global ADC_CS, ADC_CLK, ADC_DIO
    ADC_CS = cs
    ADC_CLK = clk
    ADC_DIO = dio

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ADC_CS, GPIO.OUT)
    GPIO.setup(ADC_CLK, GPIO.OUT)


def destroy():
    GPIO.cleanup()


# Using channel=0 as default for backwards compatibility.
def getResult(channel=0):
    GPIO.setup(ADC_DIO, GPIO.OUT)
    GPIO.output(ADC_CS, 0)

    GPIO.output(ADC_CLK, 0)
    GPIO.output(ADC_DIO, 1)
    time.sleep(0.000002)
    GPIO.output(ADC_CLK, 1)
    time.sleep(0.000002)
    GPIO.output(ADC_CLK, 0)

    GPIO.output(ADC_DIO, 1)
    time.sleep(0.000002)
    GPIO.output(ADC_CLK, 1)
    time.sleep(0.000002)
    GPIO.output(ADC_CLK, 0)

    GPIO.output(ADC_DIO, channel)
    time.sleep(0.000002)

    GPIO.output(ADC_CLK, 1)
    GPIO.output(ADC_DIO, 1)
    time.sleep(0.000002)
    GPIO.output(ADC_CLK, 0)
    GPIO.output(ADC_DIO, 1)
    time.sleep(0.000002)

    dat1 = 0
    for _ in range(8):
        GPIO.output(ADC_CLK, 1)
        time.sleep(0.000002)
        GPIO.output(ADC_CLK, 0)
        time.sleep(0.000002)
        GPIO.setup(ADC_DIO, GPIO.IN)
        dat1 = (dat1 << 1) | GPIO.input(ADC_DIO)

    dat2 = 0
    for i in range(8):
        dat2 = dat2 | (GPIO.input(ADC_DIO) << i)
        GPIO.output(ADC_CLK, 1)
        time.sleep(0.000002)
        GPIO.output(ADC_CLK, 0)
        time.sleep(0.000002)

    GPIO.output(ADC_CS, 1)
    GPIO.setup(ADC_DIO, GPIO.OUT)

    if dat1 == dat2:
        return dat1
    return 0


def getResult1():
    return getResult(1)


def loop():
    while True:
        res0 = getResult(0)
        res1 = getResult(1)
        print(f"res0 = {res0}, res1 = {res1}")
        time.sleep(0.4)


if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
