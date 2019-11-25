from RPi import GPIO

# Define GPIO pins
# Left motor +ve, gnd
lmPosPin = 27
lmGndPin = 24

# Right motor +ve, gnd
rmPosPin = 16
rmGndPin = 23

#########################################

def move_forward():
    GPIO.output(lmPosPin,GPIO.HIGH)
    GPIO.output(lmGndPin,GPIO.LOW)

    GPIO.output(rmPosPin,GPIO.HIGH)
    GPIO.output(rmGndPin,GPIO.LOW)

def move_backward():
    GPIO.output(lmPosPin,GPIO.LOW)
    GPIO.output(lmGndPin,GPIO.HIGH)

    GPIO.output(rmPosPin,GPIO.LOW)
    GPIO.output(rmGndPin,GPIO.HIGH)

def turn_right():
    GPIO.output(lmPosPin,GPIO.HIGH)
    GPIO.output(lmGndPin,GPIO.LOW)

def turn_left():
    GPIO.output(rmPosPin,GPIO.HIGH)
    GPIO.output(rmGndPin,GPIO.LOW)

def stop():
    GPIO.output(lmPosPin, GPIO.LOW)
    GPIO.output(lmGndPin, GPIO.LOW)

    GPIO.output(rmPosPin, GPIO.LOW)
    GPIO.output(rmGndPin, GPIO.LOW)

def __setup():
    # Set the GPIO mode
    GPIO.setmode(GPIO.BCM)

    # Set up defined GPIO pins
    GPIO.setup(lmPosPin,GPIO.OUT)
    GPIO.setup(lmGndPin,GPIO.OUT)

    GPIO.setup(rmPosPin,GPIO.OUT)
    GPIO.setup(rmGndPin,GPIO.OUT)

    GPIO.cleanup()
    
if __name__ == "__main__":
    __setup()
    stop()
    
