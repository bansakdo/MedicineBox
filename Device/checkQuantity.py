import RPi.GPIO as GPIO
import time
import subprocess
import math
from showNeopixel import showQuantity, showLoading, blink


GPIO.setwarnings(False)
Trig = [11, 10, 27, 24, 4, 15]
Echo = [9, 22, 17, 23, 3, 14]
quantityFile = "/home/pi/Medicinebox/script/quantity"

GPIO.setmode(GPIO.BCM)
for i in Trig :
    GPIO.setup(i, GPIO.OUT)
for j in Echo :
    GPIO. setup(j, GPIO.IN)


def accurateMeasureQuantity() :

    try :
        result = []
        show = showLoading()
        for slot in range(0, 6) :
            sum = 0
            measure = []
            for num in range (0, 100):
                GPIO.output(Trig[slot], False)
                time.sleep(0.1)
                GPIO.output(Trig[slot], True)
                time.sleep(0.00001)
                GPIO.output(Trig[slot], False)
                while GPIO.input(Echo[slot]) == 0:
                    start = time.time()             
                while GPIO.input(Echo[slot]) == 1:
                    stop = time.time()
                time_interval = stop - start
                distance = time_interval * 17000
                distance = round(distance, 2)

                print("distance : " + str(distance))
                measure.append(distance)
                next(show)

            
            sort = sorted(measure)[9:60]
            print("sort : ", str(sort))
            result.append(round(math.fsum(sort) / 50, 1))
            print("result : ", str(result))
        
        now = time.localtime()
        nowstr = "%04d/%02d/%02d %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
        subprocess.call("echo " + str(result) + " // " + nowstr + " > " + quantityFile, shell=True)
        #blink('b')
        showQuantity()
        return "true"
    except KeyboardInterrupt :
        showQuantity()
        GPIO.cleanup()
        print("Exit...")


def measureQuantity() :
    try :
        result = []
        show = showLoading()
        for slot in range(0, 6) :
            # while True:
            sum = 0
            measure = []
            for num in range (0, 20):
                GPIO.output(Trig[slot], False)
                time.sleep(0.1)
                GPIO.output(Trig[slot], True)
                time.sleep(0.00001)
                GPIO.output(Trig[slot], False)
                while GPIO.input(Echo[slot]) == 0:
                    start = time.time()             
                while GPIO.input(Echo[slot]) == 1:
                    stop = time.time()
                time_interval = stop - start
                distance = time_interval * 17000
                distance = round(distance, 2)

                print("distance : " + str(distance))
                measure.append(distance)
                next(show)

            
            sort = sorted(measure)[4:15]
            print("sort : ", str(sort))
            result.append(round(math.fsum(sort) / 10, 1))
            print("result : ", str(result))
        
        now = time.localtime()
        nowstr = "%04d/%02d/%02d %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
        subprocess.call("echo " + str(result) + " // " + nowstr + " > " + quantityFile, shell=True)
        blink('b')
        showQuantity()
        return "true"
    except KeyboardInterrupt :
        showQuantity()
        GPIO.cleanup()
        print("Exit...")

def getQuantity() :

    readData = str(subprocess.check_output("cat " + quantityFile, shell=True)).split('\'')[1]     # python3
    readData = str(readData).replace("\n", "")
    quantity = readData.split('//')[0].replace(" ", "")
    quantity = quantity.replace("[", "")
    quantity = quantity.replace("]", "")
    measuredTime = readData.split('//')[1].strip()
    measuredTime = measuredTime.replace("\n", "")           # python2
    measuredTime = measuredTime.replace("\\n", "")           # python3
    quantityArray = quantity.split(',')

    quantityStr = "{ "

    for i in range(0, 6) :
        quantityStr = quantityStr + "\"slot" + str(i+1) + "\" : \"" + quantityArray[i] + "\", "

    quantityStr = quantityStr + "\"time\" : \"" + measuredTime + "\" }"

    print(quantityStr)
    return quantityStr

def getArrayQuantity() :

    readData = str(subprocess.check_output("cat " + quantityFile, shell=True)).split('\'')[1]     # python3
    readData = str(readData).replace("\n", "")
    quantity = readData.split('//')[0].replace(" ", "")
    quantity = quantity.replace("[", "")
    quantity = quantity.replace("]", "")
    measuredTime = readData.split('//')[1].strip()
    measuredTime = measuredTime.replace("\n", "")           # python2
    measuredTime = measuredTime.replace("\\n", "")           # python3
    quantityArray = quantity.split(',')

    return quantityArray



arrayquantity = getArrayQuantity()

