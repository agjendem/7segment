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
    show_number(float(number)) # Test Pattern


def show_number(value):
    number = abs(value) # Remove negative signs and any decimals

    '''
    if number >= 100:
        remainder = number % 100
        post_number(remainder % 10, False)
        remainder = number % 10
        post_number(remainder, False)
        number = int(number / 10)
        post_number(number, False)
    elif number >= 10:
        remainder = number % 10
        post_number(remainder, False)
        number = int(number / 10)
        post_number(number, False)
    else:
        post_number(number, False)
        post_number("0", False)

    # Latch the current segment data
    GPIO.output(segmentLatch,GPIO.LOW)
    GPIO.output(segmentLatch,GPIO.HIGH) # Register moves storage register on the rising edge of RCK
    '''
    for a in range(numDisplays):
        post_number(number, False)
        GPIO.output(segmentLatch,GPIO.LOW)
        GPIO.output(segmentLatch,GPIO.HIGH) # Register moves storage register on the rising edge of RCK


# Given a number, or - shifts it out to the display
def post_number(number, decimal):
    segments = bytes()
    a = 1 << 0
    b = 1 << 6
    c = 1 << 5
    d = 1 << 4
    e = 1 << 3
    f = 1 << 1
    g = 1 << 2
    dp = 1 << 7

    if number == 1: segments = b | c
    elif number == 2: segments = a | b | d | e | g
    elif number == 3: segments = a | b | c | d | g
    elif number == 4: segments = b | c | f | g
    elif number == 5: segments = a | c | d | f | g
    elif number == 6: segments = a | c | d | e | f | g
    elif number == 7: segments = a | b | c
    elif number == 8: segments = a | b | c | d | e | f | g
    elif number == 9: segments = a | b | c | d | f | g
    elif number == 0: segments = a | b | c | d | e | f
    elif number == ' ': segments = 0
    elif number == 'c': segments = g | e | d
    elif number == '-': segments = g
    else : segments = 0

    ## TODO: Mistake likely here:
    #   if ((decimal segments) |= dp ):
    y = 0
    while y < 8:
        GPIO.output(segmentClock, GPIO.LOW)
        GPIO.output(segmentData, segments & 1 << (7-y))
        GPIO.output(segmentClock, GPIO.HIGH)
        y += 1


def main():
    number = 0
    while True:
        x_num=''
        print(number)
        for n in range(1):
            x_num = x_num + str(number)
        print(int(x_num))
        loop(x_num)
        time.sleep(1)
        number = number + 1
        if number > 9:
            number = 0


if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    main()
    GPIO.cleanup()

