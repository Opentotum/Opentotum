pid_plugin

  

Table of Contents


•PID tuning plugin

◦Installation


◦Use the plugin


 
PID tuning plugin


Plugin for PID tuning by tohara allow user to easily tune the PID settings for the FABtotum custom extruders. 

It basically uses the autotune procedure described here. 

Installation


First download the plugin here. 

Unzip the package, rename the folder in “pidtune” (it was “pidtune-master”), zip the new package (you will have a package “pidtune.zip”), just renaming the old file won't work. 

In the FABtotum dashboard go to “Plugins” (1) section and click “Add new” (2). 

 

Select the path of your “pidtune.zip” file, then “Install now”. 

 

The installing process will start, it will be finished in few seconds. 

 

In the “plugins” page press the green button “ Activate”, now you will see PIDtune on the left column. 

 

 

The installation process is complete. 

Use the plugin


For start the plugin press the button “Start pid tuner”(1), it will disable all printer commands.
 To start the autotuning process choose “Classic PID” method (2), then press “Start autotuning” (3) button, being careful is selected “E0”, the standard extruder port. 

 

 

The extruder temperature is set to 200°C, the hotend will start to heat up, once the target will be reached 8 times.
 At this point you will read the calculated parameters in the fields “Kp”, “Ki”, “Kd”.
Press the button “Apply parameters” to write temporarily the values on the Totumduino ram, then press “Save to EEPROM” to write permanently the values on the rom memory. 

 

The button “Get current parameters” will write in the parameters stored into the EEPROM. 
  
pid_plugin.txt · Last modified: 2015/11/05 11:46 by jj