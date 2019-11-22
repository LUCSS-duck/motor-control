class GPIO:
    def __init__():
        GPIO.BCM = "bcm"
        return True

    def setmode(mode):
        print("set mode to {}".format(mode.__name__))

    def setup(pin, mode):
        print("pin is {} mode is {}".format(pin, mode.__name__))

    def output(pin, status):
        print("pin is {} status is {}".format(pin, status.__name__))

    def cleanup():
        print("cleaned up")

    def BCM():
        return True

    def OUT():
        return True

    def HIGH():
        return True

    def LOW():
        return False
