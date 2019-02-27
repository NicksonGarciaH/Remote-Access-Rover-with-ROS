import time, os

os.system("echo 57 > /sys/class/gpio/export")   #Enable GPIO 57
os.system("echo out > /sys/class/gpio/gpio57/direction")        #GPIO 57 OUT
time.sleep(0.1)

os.system("echo 0 > /sys/class/gpio/gpio57/value")      #GPIO 57 LOW
print "LIGHTS OFF"

