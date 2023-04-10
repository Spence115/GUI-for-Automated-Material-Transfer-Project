import time
import board
import busio
import serial
import sqlite3

import adafruit_gps

uart = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=3000)

gps = adafruit_gps.GPS(uart, debug=False)

gps.send_command(b'PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0')

gps.send_command(b'PMTK220,1000')

# conn=sqlite3.connect("/home/pi/NetworkDrive/BPT.db")
# con=sqlite3.connect("/home/pi/NetworkDrive/BPT.db")
# cursor=conn.cursor()
# precursor=con.cursor()

#set range values here and uncomment
# NOTE: Be careful when dealing with negative longitudes since the if statements
# look at the location of the number with respect to zero, NOT the magnitude.
####################################

#Building 1 location coordinates
stage1_A = -10.850490
stage1_B = -10.850775

#Building 2 location coordinates
stage2_A = -10.850775
stage2_B = -10.850900

#Building 3 location coordinates 
stage3_A = 30
stage3_B = 32

#charging station
charge_A = -121.849800
charge_B = -121.851000

last_print = time.monotonic()

def track():
    
    truth = 1
    
    locationReached = 0.0
    
    time.sleep(1)

    gps.update()

    ###stage 1 
    if ((gps.longitude is not None) and (gps.longitude < stage1_A) and (gps.longitude > stage1_B)):

        locationReached = 1
        truth=0
    

    ###stage 2 
    elif ((gps.longitude is not None) and (gps.longitude < stage2_A) and (gps.longitude > stage2_B)):

        locationReached = 2
        truth = 0
    
    ###stage 3 
    elif ((gps.longitude is not None) and (gps.longitude < stage3_A) and (gps.longitude > stage3_B)):

        locationReached = 3
        truth=0
    
    ###Charging Station
    elif ((gps.longitude is not None) and (gps.longitude < charge_A) and (gps.longitude > charge_B)):

        locationReached = 4
        truth=0
   
    if(gps.longitude is not None):
        print('Latitude: {0:.6f} degrees'.format(gps.latitude))
        print('Longitude: {0:.6f} degrees'.format(gps.longitude))
    
    print('Done with search')
    print(locationReached)
    return(locationReached)
