import serial
arduinoserialdata=serial.Serial('com3',9600)
while(1==1):
    if(arduinoserialdata.inWaiting()>0):
        mydata=arduinoserialdata.readline()
        print(mydata)
