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

# Approximate vocal melody from "Yesterday" (opening phrase)
# Song is a list of tones with name and 1/duration (16 means 1/16)
SONG = [
    # Yes-ter-day,
    ["g4", 8], ["f4", 8], ["e4", 8], ["d4", 8],
    # all my trou-bles seemed so far a-way
    ["c4", 8], ["d4", 8], ["e4", 8], ["f4", 8], ["g4", 4], ["p", 16],
    # now it looks as though they're here to stay
    ["a4", 8], ["g4", 8], ["f4", 8], ["e4", 8], ["d4", 8], ["e4", 8], ["f4", 8], ["g4", 8], ["a4", 4], ["p", 16],
    # oh, I be-lieve in yes-ter-day
    ["g4", 8], ["f4", 8], ["e4", 8], ["d4", 8], ["c4", 8], ["d4", 8], ["e4", 8], ["f4", 8], ["g4", 2],
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
