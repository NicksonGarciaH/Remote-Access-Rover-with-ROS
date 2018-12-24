import time, os

os.system("echo 166 > /sys/class/gpio/export")   #Enable GPIO 166 = PIN 58
os.system("echo out > /sys/class/gpio/gpio166/direction")        #GPIO 166 OUT
time.sleep(0.1)

os.system("echo 1 > /sys/class/gpio/gpio166/value")      #GPIO 166 HIGH
print "LASER ON"
