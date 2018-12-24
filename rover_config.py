import time, os

os.system("echo 57 > /sys/class/gpio/export")   #Enable GPIO 57
os.system("echo out > /sys/class/gpio/gpio57/direction")        #GPIO 57 OUT
time.sleep(0.2)

os.system("echo 1 > /sys/class/gpio/gpio57/value")      #GPIO 57 HIGH
print "GPIO 57 ON"
time.sleep(0.2)
os.system("echo 0 > /sys/class/gpio/gpio57/value")      #GPIO 57 LOW
print "GPIO 57 OFF"
time.sleep(0.2)

os.system("echo 1 > /sys/class/gpio/gpio57/value")
print "GPIO 57 ON"
time.sleep(0.2)
os.system("echo 0 > /sys/class/gpio/gpio57/value")
print "GPIO 57 OFF"
time.sleep(0.2)

os.system("echo 1 > /sys/class/gpio/gpio57/value")
print "GPIO 57 ON"
time.sleep(0.2)
os.system("echo 0 > /sys/class/gpio/gpio57/value")
print "GPIO 57 OFF"

print "ACCEDIDO"
