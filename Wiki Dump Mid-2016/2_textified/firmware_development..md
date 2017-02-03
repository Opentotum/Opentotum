

firmware_development

  

Table of Contents


•Firmware development

◦1. Downloading FABlin


◦2. Developing FABlin: Version Control


◦3. Developing FABlin: The IDE


◦3. Flashing the firmware


 
Firmware development



1. Downloading FABlin


FABlin is available in Github, in: https://github.com/FABtotum/FABlin 

If you have GitHub installed, you can get the source directly by cloning the source: 

git clone https://github.com/FABtotum/FABlin.git//  

This generates a directory with all the code of the master branch of the repository.  

You can also download the source by going to the GitHub page of FABlin and using the “Download ZIP” option in the bottom right.  

2. Developing FABlin: Version Control


If you intend doing development of FABlin or provide bug fixes, then it is best that you create a GitHub account and use the “Fork” option in the FABlin GitHub page. This creates a copy of the repository under your username. You can develop on this copy using the flexibility that GitHub provides and when you have something to share, you can ask for a pull request of your branch. 

3. Developing FABlin: The IDE


A convenient way of developing and compiling the source is to install the Arduino IDE from http://www.arduino.cc/.  

It is not the only one, but certainly the most convenient.(note: version 1.06 seems to work, but 1.6.x does not) 

Once you have the Arduino IDE installed, you can open the “.ino” file in FABlin to load the source code of the project. Then you can do your modifications and compile the code using the “checked” icon in the top left of the Arduino IDE window.  

One thing to take into account when using the Arduino IDE is that compiling is detached from saving, you can compile a modified file without saving it. I personally do not like this behaviour, and for this reason I use an external editor (Kate, a linux UI editor), while I still use Arduino IDE for compiling. 

Before compiling, make sure you have selected the right target chip in the menu. The totumduino has an ATMEGA 1280. If you compile for another chip it won't work.  

The Arduino IDE generates a file with the same name as the project and extension “.cpp.hex” in the temporary directory. In Linux is in /tmp/buildNNNNNNN/, in windows it is apparently in “Windows/Users/me/Appdata/Local/Temp”.  

The Arduino IDE generates one of this “build” folders for every execution, and does not always clean up afterwards, so always check the date and time of the generated firmware before uploading, or you may be uploading the wrong firmware (and old version). 

3. Flashing the firmware


The easiest way to flash a new firmware is to upload the firmware file to  /var/www/build/Marlin.cpp.hexand use the built-in flasher.  

In Linux you can do this like this:  

scp Marlin.cpp.hex root@fabtotum:/var/www/build 

In Windows you should be able to use WinSCP to copy the file  Marlin.cpp.hex to the directory /var/www/build/  

Make sure the file name is “Marlin.cpp.hex”. Linux is case sensitive.  

After having copied the firmware to the FABtotum, go to: http://fabtotum/recovery/flash.php and click in flash local file. Wait until the web interface indicates to you that the firmware has been properly flashed (it beeps a couple of times in between).  

Flashing Firmware from the raspberry 

Uploaded your firmware to /var/www/build/ and connect to your FAB with a ssh terminal (search putty for win o just open a terminal on linux/mac) 

ssh root@fabtotum 

pass: fabtotum 

cd /var/www/build 

/usr/bin/avrdude -D -q -V -p atmega1280 -C /etc/avrdude.conf -c arduino -b 57600 -P /dev/ttyAMA0 -U flash:w:Marlin.cpp.hex:i 
  
firmware_development.txt · Last modified: 2015/12/22 19:09 by darkfibre
 
--------------------------------------------------------------------------------
