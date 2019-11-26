# Remote-Access-Rover-with-ROS
A repository for a 6-wheel rocker bogie rover, based on Robotic Operative System [ROS][ros] and python to control its perception and action systems.
This repository contents: 
- source codes.
- dev scripts (Python | ROS)
Watch the YouTube video [here][vid]
[Doc]

## Hardware elements
- Nvidia Jetson TK1: [Lib][jet]
- Ion Motion Roboclaw, Dual DC motor driver: [Lib][lib-rc]
- Pololu USB servo Control: [POL-1353][pol]
- Logitech Wireless Gamepad F710 
- PC host running Ubuntu

## Software requirements
- Python 2.7.15
- Rviz from ROS
- ROS [Kinetic][kin] for Ubuntu 16.04 or [Indigo][ind] for Ubuntu 14.04 on user PC.
- ROS [Indigo][ind-j] for Ubuntu 14.04 (armhf) on Jetson TK1.

## Getting Started on Jetson TK1
The following steps describe how to configure the Jetson TK1.
- Install [ROS][ind-j]
- Install nano: `sudo apt-get install nano`
- Install Git: `sudo apt-get install git-core`
- Install [Hamachi][ham]
- Remove sudo pass:
`sudo visudo`
```
# Members of the admin group may gain root privileges
%admin ALL=(ALL) ALL
# Allow members of group sudo to execute any command
%sudo   ALL=(ALL:ALL) ALL
```
And replace those lines for these:
```
# Members of the admin group may gain root privileges
%admin ALL=(ALL) NOPASSWD: ALL
# Allow members of group sudo to execute any command
%sudo ALL=(ALL:ALL) NOPASSWD: ALL
```
- USB Rules
Look for your USB devices info:
`udevadm info -a -n /dev/ttyUSB1 | grep`
Create this file with your idVendor and idProduct info:
`sudo nano /etc/udev/rules.d/99-robot.rules`

```
SUBSYSTEM=="tty", ATTRS{idVendor}=="03eb", ATTRS{idProduct}=="2404", SYMLINK+="tty_roboclaw"
SUBSYSTEM=="tty", ATTRS{idVendor}=="0424", ATTRS{idProduct}=="9514", SYMLINK+="tty_pololu"
```
Save and run:
`sudo udevadm trigger`
`sudo chmod 777 /dev/tty_roboclaw`
`sudo chmod 777 /dev/tty_pololu`

#### Installing USB camera on ROS
- Plug in the USB camera and check if it was recognized by system:
`lsusb `
`ls /dev | grep video*`

- Install usb_cam ROS node:
`sudo apt install ros-indigo-usb-cam`
 
#### Functions to add on Jetson's .bashrc file
`nano .bashrc`
```
source /opt/ros/indigo/setup.bash

function arm {
        sudo chmod 777 /dev/tty_pololu
        python /home/ubuntu/Desktop/Mercury/arm.py
        sleep 1
        echo $"Arm OK..."
}

function exportar {
        export ROS_IP = {JetsonIP}
        export ROS_MASTER_URI = http://{pcIP}:11311
}

# If want to connect through hamachi
function exportar_hamachi {
        export ROS_IP = {JetsonHamachiIP}
        export ROS_MASTER_URI=http://{pcHamachiIP}:11311
}

#Launch main webcam
function webcam {
	roslaunch usb_cam usb_cam-test.launch &
        sleep 5
        echo $"Main camera ready..."
}

function run {
        sudo chmod 777 /dev/tty_roboclaw
        source /home/ubuntu/rbcw_ws/devel/setup.bash
        roslaunch roboclaw_node roboclaw.launch &
        sleep 3
        echo $"Run Launched"
}

function kinect {
	roslaunch freenect_launch freenect.launch
}

function ekf {
        python ~/Desktop/Mercury/ekf.py
}

function imu_node {
	sudo chmod 777 /dev/ttyUSB0
	source /home/ubuntu/xsens_ws/devel/setup.bash
	roslaunch xsens_driver xsens.launch
}


# Main function
function rover {
        roscore &
        sleep 4
        piloto &
        echo $"Launched piloto"
        sleep 2
        run &
        sleep 2
        echo $"Ready..."
}

sudo python /home/ubuntu/Desktop/Mercury/bash_config.py
```
## Getting Started on host PC
- Install ros according to your ubuntu version, in this case Ubuntu 16.04.
- Install hamachi and haguichi.
#### Configuring a Linux-Supported Joystick with ROS
- Install the package:
`sudo apt-get install ros-kinetic-joy`
- The joystick will be referred to by jsX: `ls /dev/input`
- You can test it by running:
`sudo jstest /dev/input/jsX`
Move the joystick around to see the data change. 
- Give permissions on the joystick port:
`sudo chmod a+rw /dev/input/jsX`
- To start the joy node:
`roscore`
`rosparam set joy_node/dev "/dev/input/jsX"`
`rosrun joy joy_node`
To see the data from the joystick:
`rostopic echo joy`

#### Functions to add on PC's .bashrc file
```
source /opt/ros/kinetic/setup.bash

function pilot
{
  ls -l /dev/input/jsX
  sudo chmod a+rw /dev/input/jsX
  rosparam set joy_node/dev "/dev/input/jsX"
  rosrun joy joy_node &
 }

# If want to connect through hamachi
function exportar_hamachi 
{
        export ROS_IP = {pcIP}
}

function exportar
{
  export ROS_IP = {pcIP}
}

# To access Jetson webcam image
function webcam
{
	python ~/cam_bridge.py
}
```


### Autors
* Nickson Garcia H.  - (2420132006@estudiantesunibague.edu.co)
* Cristian Molina H. - (2420132009@estudiantesunibague.edu.co)
* Harold F. Murcia.  - (harold.murcia@unibague.edu.co )


[ros]: <http://www.ros.org/>
[lib-rc]: <http://www.basicmicro.com/downloads>
[pol]: <https://www.pololu.com/product/1353>
[jet]: <https://developer.nvidia.com/embedded/downloads#?tx=$product,jetson_tk1$software,l4t-tk1>
[kin]: <http://wiki.ros.org/kinetic/Installation/Ubuntu>
[ind]: <http://wiki.ros.org/indigo/Installation/Ubuntu>
[ind-j]: <http://wiki.ros.org/indigo/Installation/UbuntuARM>
[ham]: <https://medium.com/@KyleARector/logmein-hamachi-on-raspberry-pi-ad2ba3619f3a>
[vid]: <https://www.youtube.com/watch?v=stQqyb9inXY&t=333s>
[Doc]: <https://repositorio.unibague.edu.co/jspui/bitstream/20.500.12313/1296/1/Trabajo%20de%20grado.pdf>
