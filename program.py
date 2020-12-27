"""""
Code by: Charanpreet Singh
Email: Charanmakkar@gmail.com
Linkedin profile: https://www.linkedin.com/in/charanpreet-singh-a29949133/
Development date Aug 19, 2020
Final editing done on Aug 25, 2020
Github Upload: Dec 27, 2020
"""""

##Importing required libraries
import minimalmodbus as mm, serial, time


""""
Defining all functions and parameteres start from here.
all the defined libraries are defined above this note.
"""
####Function to set parameters for communicattion
def setParameters(x,y,z):
    try:
        instrument = mm.Instrument(x , 3 , debug = False)
        instrument.serial.baudrate = y
        instrument.address = z
        instrument.serial.timeout  = 1
        instrument.serial.parity   = serial.PARITY_NONE
        instrument.mode = mm.MODE_RTU
        print(instrument)
        return instrument
    except:
        #if no device found
        print("Device NOT coneected")

####Function to read data from RS485 connnection made at a specific register and 
def readint(a):
    try:
        #data = instrument.read_register(a,10,3)
        data = instrument.read_register(a)
        print(str(data))
        return data
    except IOError:
        print("Failed to read from instrument")

#Set Parameter of RS485 communication here
#instrument = setParameters('COM port name', Baud rate, Slave Address)
instrument = setParameters('COM21', 19200, 111)


####Loop that repeats infinite times
while (1):
    try:
        #Put register value inside the brackets (As per given in datasheet of controller/PLC)
        a = readint(17)
        print(c)
    except:
        #if wrong register value or No Connected
        print("Error while data from register")
   
    try:
        #Put register value inside the brackets (As per given in datasheet of controller/PLC)
        b = readint(19)
        print(b)
    except:
        #if wrong register value or No Connected
        print("Error while data from register")
    
    #Time delay of (1 = 1 second) 1 second after each run
    time.sleep(1)

    #To seperate readings after each run
    print("__" * 40)
