

pid_tuning

 
PID tuning of DIY nozzle mods


To calibrate the nozzle thermistor on a custom head you need to start from room temperature and establish an SSH connection.
 Use the M303 comand to start the PID autotune procedure 


M303 E0 S200 C8 

 This will calculate -for example- the PID of extruder 0 (the head) heating it up to 200°C with 8 iterations.

Note: You may want to do this in Minicom or another serial emulator to see the realtime output.
 You will loose the final part of the output due to timeouts if you do this in the JOG menu.
 from ssh: minicom -b115200 -D/dev/ttyAMA0 

 At the end of the script you'll get the kp, Ki,Kd values, just plug them in here:
 e.g (P=14.64 I=3 D=64.71)

M301 P14.63 I3 D64.71 

this will override the EEPROM saved values. 

(The standard values used for the hybrid head with the J-Head hot end are the following: P15 I5 D30 ) 


 Then from the Jog try to increase the temp from room temp to 200 and watch it rise.
 you don't want the extruder temperature to fluctuate or to be very slow in the final approach to target temp. 

A nifty python script can be used to log the temperature curve to a file: temp_logger
 To run it put temp_logger.py under /var/www/recovery/python/  and execute it.
 

sudo python /var/www/recovery/python/temp_logger.py 190 output.log  
 

(Where 190 is the target temperature, you can vary it) 

if you are ok with the result just save your config to EEPROM and you are done

M500 

 Verify values are saved with

M503 

External resources


For see the teory about PID control, check the wikipedia page here. 

For the automatic tuning using the plugin look this page. 
  
pid_tuning.txt · Last modified: 2016/05/09 15:06 by fabteam
 
--------------------------------------------------------------------------------
