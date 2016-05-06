import RPi.GPIO as GPIO
import time

r=27
g=22
b=17
white=[1,1,1]

Freq=100
speed=.0005

def color(R,G,B,on_time,RED, GREEN, BLUE):
        RED.ChangeDutyCycle(R)
        GREEN.ChangeDutyCycle(G)
        BLUE.ChangeDutyCycle(B)
        time.sleep(on_time)

        RED.ChangeDutyCycle(1)
        GREEN.ChangeDutyCycle(1)
        BLUE.ChangeDutyCycle(1)


def initializeGPIO():

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

        GPIO.setup(r,GPIO.OUT)
        GPIO.setup(g,GPIO.OUT)
        GPIO.setup(b,GPIO.OUT)

        GPIO.output(r,GPIO.LOW)
        GPIO.output(g,GPIO.LOW)
        GPIO.output(b,GPIO.LOW)


        RED = GPIO.PWM(r,Freq)
        GREEN = GPIO.PWM(g,Freq)
        BLUE = GPIO.PWM(b,Freq)

        RED.start(100)
        GREEN.start(100)
        BLUE.start(100)
        return (RED, GREEN, BLUE)
        
def rainbow():
	print("RAINBOW")
	RED, GREEN, BLUE = initializeGPIO()
        for x in range(1,-1,-1):
                for y in range(1,-1,-1):
                        for z in range(1,-1,-1):
                                print(x,y,z)
                                for i in range(100,-1,-1):
                                        color((x*i),(y*i),(z*i),speed,RED, GREEN, BLUE)
                                for i in range(0,101,1):
                                        color((x*i),(y*i),(z*i),speed,RED, GREEN, BLUE)

        GPIO.cleanup()

def shade(x,y,z):
        speed=.005
	print("WHITE")
	RED, GREEN, BLUE = initializeGPIO()
        print(x,y,z)
        for i in range(100,-1,-1):
                color((x*i),(y*i),(z*i),speed,RED, GREEN, BLUE)

        GPIO.cleanup()


shade(white[0],white[1],white[2])                                  
