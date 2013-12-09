import RPi.GPIO as GPIO
import time
# blinking function
def blink(pin):
        GPIO.output(7,GPIO.HIGH)
        time.sleep(1)
        GPIO.output(7,GPIO.LOW)
        time.sleep(1)
        return
# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BOARD)
# set up GPIO output channel
GPIO.setup(7, GPIO.OUT)
# blink GPIO17 50 times
for i in range(0,50):
        blink(11)
GPIO.cleanup() 
