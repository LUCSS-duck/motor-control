from RPi import GPIO

# Define GPIO pins
# Left motor +ve, gnd
lmPosPin = 27
lmGndPin = 24

# Right motor +ve, gnd
rmPosPin = 16
rmGndPin = 23

# Axle motor +ve, gnd
amPosPin = 0
amGndPin = 0

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

def turn_axle_right():
    GPIO.output(amPosPin,GPIO.HIGH)
    GPIO.output(amGndPin,GPIO.LOW)

def turn_axle_left():
    GPIO.output(amPosPin,GPIO.LOW)
    GPIO.output(amGndPin,GPIO.HIGH)

def move_right():
    turn_axle_right()
    move_forward()

def move_left():
    turn_axle_left()
    move_forward()

def move_back_right():
    turn_axle_right()
    move_backward()

def move_back_left():
    turn_axle_left()
    move_backward()

def center_axle():
    GPIO.output(amPosPin,GPIO.LOW)
    GPIO.output(amGndPin,GPIO.LOW)

def stop():
    GPIO.output(lmPosPin, GPIO.LOW)
    GPIO.output(lmGndPin, GPIO.LOW)

    GPIO.output(rmPosPin, GPIO.LOW)
    GPIO.output(rmGndPin, GPIO.LOW)

    center_axle()

def __setup():
    # Set the GPIO mode
    GPIO.setmode(GPIO.BCM)

    # Set up defined GPIO pins
    GPIO.setup(lmPosPin,GPIO.OUT)
    GPIO.setup(lmGndPin,GPIO.OUT)

    GPIO.setup(rmPosPin,GPIO.OUT)
    GPIO.setup(rmGndPin,GPIO.OUT)

    GPIO.setup(amPosPin,GPIO.OUT)
    GPIO.setup(amGndPin,GPIO.OUT)

    GPIO.cleanup()
    
if __name__ == "__main__":
    __setup()
    stop()
    
