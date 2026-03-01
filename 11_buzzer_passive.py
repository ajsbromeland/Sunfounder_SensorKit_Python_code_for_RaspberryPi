#!/usr/bin/env python3
import time

import RPi.GPIO as GPIO

BuzzerPin = 11  # pin11
SPEED = 1

# List of tone names with frequency
TONES = {
    "c6": 1047,
    "b5": 988,
    "a5": 880,
    "g5": 784,
    "f5": 698,
    "e5": 659,
    "eb5": 622,
    "d5": 587,
    "c5": 523,
    "b4": 494,
    "a4": 440,
    "ab4": 415,
    "g4": 392,
    "f4": 349,
    "e4": 330,
    "d4": 294,
    "c4": 262,
}

# Song is a list of tones with name and 1/duration (16 means 1/16)
SONG = [
    ["e5", 16], ["eb5", 16],
    ["e5", 16], ["eb5", 16], ["e5", 16], ["b4", 16], ["d5", 16], ["c5", 16],
    ["a4", 8], ["p", 16], ["c4", 16], ["e4", 16], ["a4", 16],
    ["b4", 8], ["p", 16], ["e4", 16], ["ab4", 16], ["b4", 16],
    ["c5", 8], ["p", 16], ["e4", 16], ["e5", 16], ["eb5", 16],
    ["e5", 16], ["eb5", 16], ["e5", 16], ["b4", 16], ["d5", 16], ["c5", 16],
    ["a4", 8], ["p", 16], ["c4", 16], ["e4", 16], ["a4", 16],
    ["b4", 8], ["p", 16], ["e4", 16], ["c5", 16], ["b4", 16], ["a4", 4],
]


def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(BuzzerPin, GPIO.OUT)


def playTone(pwm, tone):
    duration = 1.0 / (tone[1] * 0.25 * SPEED)

    if tone[0] == "p":
        time.sleep(duration)
    else:
        frequency = TONES[tone[0]]
        pwm.ChangeFrequency(frequency)
        pwm.start(50)
        time.sleep(duration)
        pwm.stop()


def run():
    pwm = GPIO.PWM(BuzzerPin, 440)
    pwm.start(50)
    for tone in SONG:
        playTone(pwm, tone)


def destroy():
    GPIO.output(BuzzerPin, GPIO.HIGH)
    GPIO.cleanup()


if __name__ == '__main__':
    setup()
    try:
        run()
    except KeyboardInterrupt:
        destroy()
    finally:
        GPIO.cleanup()
