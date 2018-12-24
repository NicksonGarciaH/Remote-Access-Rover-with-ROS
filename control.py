#!/usr/bin/env python
# Software License Agreement (BSD License)
#
# Copyright (c) 2008, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of Willow Garage, Inc. nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# Revision $Id$

## Simple talker demo that published std_msgs/Strings messages
## to the 'chatter' topic

import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Joy
import time, os
from roboclaw import Roboclaw

rc = Roboclaw("/dev/tty_roboclaw",115200)
rc.Open()
address = 0x80
int_OK=1

def callback(data):
    buttons = data.buttons;
    axes = data.axes
    if int_OK == 1:
	outs(buttons, axes)
	move(buttons, axes)
    #rospy.loginfo(rospy.get_caller_id() + "I heard %s", data)
def callback2(data):
    if data.data == "Internet FAIL":
    	rc.ForwardBackwardM1(address,64)
    	rc.ForwardBackwardM2(address,64)
	int_OK=0
    else:
	int_OK=1
def outs(buttons,axes):
	
	if buttons[4]==1 and buttons[0]==1:
        	#Laser ON
		os.system("sudo python /home/ubuntu/Desktop/Mercury/laser_on.py")
	elif buttons[4]==1 and buttons[5]==1:
		#Leds ON
		os.system("sudo python /home/ubuntu/Desktop/Mercury/leds_on.py")
	elif buttons[4]==1 and buttons[1]==1:
        	#Lights OFF
		os.system("sudo python /home/ubuntu/Desktop/Mercury/lights_off.py")
	elif axes[2]==-1 and axes[5]==-1 and buttons[0]==1 and buttons[2]==1:
        	os.system("sudo reboot")
def move(buttons, axes):
    ML = axes[0];
    MR = axes[3];
    #rospy.loginfo("Left Motor %s", ML)
    #rospy.loginfo("Right Motor %s", MR)
    if(buttons[4]==1):
        G=50.0 # max=64
    else:
        G=0.0
    U_R =int(MR*G)
    U_L =int(-ML*G)
    rc.ForwardBackwardM2(address,64+U_R+U_L)	#1/4 power forward
    rc.ForwardBackwardM1(address,64+U_R-U_L)	#1/4 power backward


def controller():
    rospy.init_node('control', anonymous=True)
    rospy.Subscriber("/joy", Joy, callback) 
    rospy.Subscriber("/url_test", String, callback2)
    rospy.spin()



if __name__ == '__main__':
    try:
        controller()
    except rospy.ROSInterruptException:
        pass
