#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import signal
import sys

# GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

segmentClock = 11
segmentLatch = 13
segmentData = 14
numDisplays = 7
numSegments = 8  # 7 + dot

GPIO.setup(segmentClock, GPIO.OUT)
GPIO.setup(segmentData, GPIO.OUT)
GPIO.setup(segmentLatch, GPIO.OUT)

GPIO.output(segmentClock, GPIO.LOW)
GPIO.output(segmentData, GPIO.LOW)
GPIO.output(segmentLatch, GPIO.LOW)


def signal_handler(sig, frame):
    print('Shutting down displays')
    GPIO.cleanup()
    sys.exit(0)


def loop(number):
    show(float(number))  # Test Pattern


def show(value):

    for symbol in value:
        print("Displaying symbol: {}".format(symbol))
        post_character(symbol)
        GPIO.output(segmentLatch, GPIO.LOW)
        GPIO.output(segmentLatch, GPIO.HIGH)  # Register moves storage register on the rising edge of RCK


# Given a number, or - shifts it out to the display
def post_character(symbol, show_decimal=False):
    segments = bytes()
    a = 1 << 0
    b = 1 << 6
    c = 1 << 5
    d = 1 << 4
    e = 1 << 3
    f = 1 << 1
    g = 1 << 2
    dp = 1 << 7

    if symbol == 1: segments = b | c
    elif symbol == 2: segments = a | b | d | e | g
    elif symbol == 3: segments = a | b | c | d | g
    elif symbol == 4: segments = b | c | f | g
    elif symbol == 5: segments = a | c | d | f | g
    elif symbol == 6: segments = a | c | d | e | f | g
    elif symbol == 7: segments = a | b | c
    elif symbol == 8: segments = a | b | c | d | e | f | g
    elif symbol == 9: segments = a | b | c | d | f | g
    elif symbol == 0: segments = a | b | c | d | e | f
    elif symbol == "1": segments = b | c
    elif symbol == "2": segments = a | b | d | e | g
    elif symbol == "3": segments = a | b | c | d | g
    elif symbol == "4": segments = b | c | f | g
    elif symbol == "5": segments = a | c | d | f | g
    elif symbol == "6": segments = a | c | d | e | f | g
    elif symbol == "7": segments = a | b | c
    elif symbol == "8": segments = a | b | c | d | e | f | g
    elif symbol == "9": segments = a | b | c | d | f | g
    elif symbol == "0": segments = a | b | c | d | e | f
    elif symbol == "A" or "a": segments = a | b | c | e | f | g
    elif symbol == "B" or "b": segments = a | b | c | d | e | f | g
    elif symbol == "S" or "s": segments = a | c | d | f | g
    elif symbol == "U" or "u": segments = b | c | d | e | f
    elif symbol == ' ': segments = 0
    elif symbol == 'c': segments = g | e | d
    elif symbol == '-': segments = g
    else: segments = 0

    if show_decimal:
        segments |= dp

    y = 0
    while y < numSegments:
        GPIO.output(segmentClock, GPIO.LOW)
        GPIO.output(segmentData, segments & 1 << (7-y))
        GPIO.output(segmentClock, GPIO.HIGH)
        y += 1


def main():
    while True:
        show("-123 45")
        time.sleep(2)
        show("SB1 U")
        time.sleep(2)


if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    main()
    GPIO.cleanup()

