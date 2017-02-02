probe_angle_calibration

  

Table of Contents


•Probe Angles Calibration
◦ 
◾The Jog Menu


◾Set the Extended Angle (open position)


◾Set the Retracted Angle (closed position)


◾Test your settings



 
Probe Angles Calibration


Due to the way angles are stored in the different versions of FabUI,
Firmware updates might cause the probe angle to change.   

Do not change/unscrew the probe or modify the hardware. 

Changing the probe angle has a simple software solution. 

--------------------------------------------------------------------------------

The Jog Menu


To calibrate your probe's angles, you'll need to type commands in the console
 part of the Jog Menu (where it's says “MDI:Write commands”) 

The default values are : 

• Probe extended (open) value: 126


• Probe retracted (closed) value: 27


To write multiple lines of commands in the console, 
 just use shift + enter. 

Few words before you start : 
 The M711 & M712 commands set and save the values for you. 
 No need to use M500 to save the new settings once you're done ! 

--------------------------------------------------------------------------------

Set the Extended Angle (open position)


You can set the angle for the extended (open) position with : 
M711 Sxxx
where xxx is the extended (open) angle value. 

The commands to run : 
M711 S126
M401press ENTER
The probe will open to the desired position. 
 Change the value with +/- 5. Keep pressing enter with 
 adjusted values (e.g 120,122,125) until you find the one that is perfectly vertical. 

--------------------------------------------------------------------------------

Set the Retracted Angle (closed position)


You can set the angle for the retracted (closed) position with : 
M712 Sxxx
where xxx is the retracted (closed) angle value. 

The commands to run : 
M712 S27
M402press ENTER
The probe will close to the desired position. 
 Change the value with +/- 5. Keep pressing enter with 
 adjusted values (e.g 30,25,22) until you find the one that is perfectly horizontal 
and does put too much stress on the servo (DO NOT go below 20 unless absolutly necessary). 

--------------------------------------------------------------------------------

Test your settings


You can now test your new settings. 

To extend (open) the probe : 
M401
To raise (close) the probe : 
M402  
probe_angle_calibration.txt · Last modified: 2016/05/09 10:13 by jj