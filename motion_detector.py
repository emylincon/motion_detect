# This a property of LSBU developed by Emeka Ugwuanyi

import time
import os
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)

led1 = 17
pirPin = 26

GPIO.setup(led1,GPIO.OUT)
GPIO.setup(pirPin, GPIO.IN)

def LIGHTS(pirPin):
    """Turns LEDS On and Off"""
    print("Motion Detected!")
    print("Lights on")
    GPIO.output(led1,GPIO.HIGH)

    time.sleep(2)

    print("Light off")
    GPIO.output(led1,GPIO.LOW)
    os.system('clear')
    print('Checking for Change in Motion in 2 secs...')
    time.sleep(2)


def motion_detect():
    try:
        GPIO.add_event_detect(pirPin, GPIO.RISING, callback=LIGHTS)
        while 1:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Quit")
        GPIO.cleanup()


def main():
    print("Motion Sensor Alarm (CTRL+C to exit)")
    time.sleep(3)
    print("Ready")
    motion_detect()


if __name__ == "__main__":
    main()

