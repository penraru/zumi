import smbus
import time

ARRAYMAX = 20
bus = smbus.SMBus(1)
address = 0x04
outboundArray=[]

def writeString():
	j = len(outboundArray)
	if j > ARRAYMAX:
		j = ARRAYMAX
		outboundArray[ARRAYMAX-1] = "\n"
	for i in range(0,j):
		bus.write_byte(address, ord(outboundArray[i]))
		time.sleep(0.02)
	return -1

def readString():
        number = bus.read_byte(address)
        number = chr(number)
        return number

while 1:
        var = raw_input("Enter a string: ")
        if var == "exit":
                break
	word = str(var)
	outboundArray = list(word)
	outboundArray.append("\n")
	
        writeString()
        print "RPI: Hi Arduino, I sent you", outboundArray
        #time.sleep(0.1)

        #number = readString()
        #print "Arduino: Hey RPI, I received", number

