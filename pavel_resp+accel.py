import bitalino
import numpy
import time

macAddress1 = "20:17:09:18:58:62"
 
test = bitalino.BITalino(macAddress1)
time.sleep(1)

srate = 1000
nframes = 100
resp_threshold = 500
acc_threshold = 580
alarm = 0
alarm_played = 0

test.start(srate, [1,3])
print ("START")

try:
    while True:

        data = test.read(nframes)
        if numpy.mean(data[:, 1]) < 1: break
        
     
        r= data[:, 5]
        y= data[:, 6]
        resp_sm = numpy.mean(r)
        acc_sm = numpy.mean(y)

        if resp_sm > resp_threshold and acc_sm > acc_threshold:
            print("act")
            alarm = 1
        else: 
            print(resp_sm,acc_sm)
            alarm = 0
            

        if alarm == 1 and alarm_played == 0:
            test.trigger([0,1])
            alarm_played = 1
            
        if alarm == 0 and alarm_played == 1:
            test.trigger([0,0])
            alarm_played = 0

                
finally:
    print ("STOP")
    test.stop()
    test.close()