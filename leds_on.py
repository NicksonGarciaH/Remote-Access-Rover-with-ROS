import time, os

os.system("echo 1 > /sys/class/gpio/gpio57/value")      #GPIO 57 HIGH
print "LEDS ON"
