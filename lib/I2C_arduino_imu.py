import smbus
import time
import math

#MPU6050 STUFF
# Register
power_mgmt_1 = 0x6b
power_mgmt_2 = 0x6c

# Initialize constants
SAMPLERATE = 10
 
# Initialize variables
millis = int(round(time.time()*1000))
angle = 0.0
angleNew = 0.0

bus = smbus.SMBus(1)
addressArduino = 0x04
#This is the Arduino Nano Address

addressIMU = 0x68
#Address for the MPU6050 Accelerometer/Gyroscope
 
changeInTime = 0

prevAngleX = 0
prevAngleY = 0
prevAngleZ = 0

imuTimer = 0
def writeCharacterArduino(value):
        #pass in a ASCII character turn it into Byte
        bus.write_byte(addressArduino, ord(value))
        return -1

def readCharacterArduino():
        #read the byte sent over to us from this specific address
        character = bus.read_byte(addressArduino)
        #convert byte into character
        character = chr(character)
        return character

#---------------------------------------------

def read_byte(reg):
        return bus.read_byte_data(addressIMU, reg)
 
def read_word(reg):
        h = bus.read_byte_data(addressIMU, reg)
        l = bus.read_byte_data(addressIMU, reg+1)
        value = (h << 8) + l
        return value
 
def read_word_2c(reg):
        val = read_word(reg)
        if (val >= 0x8000):
                return -((65535 - val) + 1)
        else:
                return val

def dist(a,b):
        return math.sqrt((a*a)+(b*b))
   
            
def get_gyroSpeed():
        angspeedZ = read_word_2c(0x47)/ 131.0
        angspeedX = read_word_2c(0x43)/ 131.0
        angspeedY = read_word_2c(0x45)/ 131.0
        return angspeedZ, angspeedX, angspeedY

def calc_gyroAngles(angular_speedZ,angular_speedX,angular_speedY):
        global prevAngleX,prevAngleY,prevAngleZ, imuTimer
        
        angleX = prevAngleX + (angular_speedX*imuTimer)
        angleY = prevAngleY + (angular_speedY*imuTimer)
        angleZ = prevAngleZ + (angular_speedZ*imuTimer)
        prevAngleX = angleX
        prevAngleY = angleY
        prevAngleZ = angleZ
        
        return angleX, angleY, angleZ


def get_accAngles():
    
        accX = read_word_2c(0x3b)/ 16384.0
        accY = read_word_2c(0x3d)/ 16384.0
        accZ = read_word_2c(0x3f)/ 16384.0
        accYangle = math.degrees(math.atan2(accX,dist(accY,accZ)))
        accXangle = math.degrees(math.atan2(accY,dist(accX,accZ)))
        return accYangle, accXangle


#---------------------------------------------
#need this line to get IMU out of sleep mode
bus.write_byte_data(addressIMU, power_mgmt_1, 0)

while (1):
        #speed = get_gyroSpeed(millis)
        #changeInTime = int(round(time.time()*1000))
        initialTime = ((time.time()*1000))
        '''
        if ( changeInTime -  ) >= SAMPLERATE:
                #angspeedZ, angspeedX, angspeedY
                z,x,y = get_gyroSpeed()
                #angular_speedZ,angular_speedX,angular_speedY
                angle = calc_gyroAngles(z,x,y)
                acc = get_accAngles()
                print(angle, " ", changeInTime)
        '''
        
        finalTime = ((time.time()*1000))
        changeInTime = finalTime - initialTime 
        imuTimer = changeInTime + imuTimer

        if (imuTimer > SAMPLERATE):
                z,x,y = get_gyroSpeed()
                #angular_speedZ,angular_speedX,angular_speedY
                angle = calc_gyroAngles(z,x,y)
                acc = get_accAngles()
                print(acc)
                #print(imuTimer)
                imuTimer = 0
        writeCharacterArduino("H")
        #time.sleep(0.1)
        print(readCharacterArduino())

 
                         
        

  
        

