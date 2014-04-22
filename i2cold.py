#!/usr/bin/python3.2
import smbus
import time
import array
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM) # on sélectionne le brchage BCM
GREEN_LED = 18
RED_LED = 23

BUTTON1 = 24
# Dernier état connu du bouton
# Par defaut: le bouton n'est pas considéré comme activé
BUTTON1_STATE = False
GPIO.setup(GREEN_LED, GPIO.OUT)
GPIO.setup(RED_LED, GPIO.OUT)
GPIO.setup(BUTTON1, GPIO.IN)

bus = smbus.SMBus(1)

# This is the address we setup in the Arduino Program
address = 0x04

def writeNumber(value):
	bus.write_byte(address, value)
	return -1
	
def writeString(value):
    #bus.write_byte(address, value)
    bus.write_i2c_block_data(address, 0, value)
    # bus.write_byte_data(address, 0, value)
    return -1
    
def readString():
	
    rvalue = bus.read_i2c_block_data(address, 0)
    # bus.write_byte_data(address, 0, value)
    return rvalue

def readNumber():
    number = bus.read_byte(address)
    # number = bus.read_byte_data(address, 1)
    return number
    
def convertStrToListHex(strChaine):
   lstHex = []
   for c in strChaine:
      lstHex.append(ord(c))
   return lstHex    

#var = "Test"
#var2 = convertStrToListHex(var)
#writeString(var2)
#bus.write_byte(address, 3)
#print "RPI: Hi Arduino, I sent you ", var2
# sleep one second
#time.sleep(1)

#zvalue = readString()
#print "Arduino: Hey RPI, I received a digit ", zvalue
#print
z=0
print "Init "
for i in range(0,7):
		writeNumber(z)
		number = readNumber()
		time.sleep(1)
		z=z+1
		print " ",str(unichr(number))
while True:
 
		# -- Lecture avec déparasitage logiciel
        # Si le bouton est pressé, la broche GPIO est raccordée
        #   à la masse. Le GPIO est donc à LOW (bas).
        #   Bouton pressé -> Input = LOW = False         
        gpioRead1 = GPIO.input( BUTTON1 )
        state1    = not(gpioRead1)
        # SI changer d'etat ALORS refaire lecture de déparasitage
        if( state1 != BUTTON1_STATE ):
                # - attendre 10ms
                time.sleep( 10 / 1000 )
                # faire une 2ieme lecture
                gpioRead2 = GPIO.input( BUTTON1 )
                state2 = not(gpioRead2)
                # SI les deux lectures concordent
                # ALORS memoriser le nouvel etat du bouton
                if( state1 == state2 ):
                        BUTTON1_STATE = state2


        # -- Programme principal --
        # SI le bouton est pressé
        # ALORS allumer la LED verte  
        if( BUTTON1_STATE == True ):
                GPIO.output(GREEN_LED, False)
                GPIO.output(RED_LED, True)
        else:
                GPIO.output(GREEN_LED, True)
                GPIO.output(RED_LED, False)

	var = input("Enter 1 - 9: ")
	if not var:
		continue    
   # writeNumber(var)
    #print "RPI: Hi Arduino, I sent you ", var
    # sleep one second
    
    #time.sleep(1)
	z=0
	print "Arduino: Hey RPI, I received a digit "
	for i in range(0,8):
		writeNumber(z)
		number = readNumber()
		time.sleep(2)
		z=z+1
		print " ",str(unichr(number))

	#var = input("Enter 1 - 9: ")
    #if not var:
     #   continue	