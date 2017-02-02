

spindle

 
Spindle


The spindle is the part that holds the milling bit. It's connected to a DC brushess motor that can turn as fast as 14000 rpm. 

It accept 1/8“ bits (3 to 3,5mm) 


 You can control it in the “Jog” panel with those commands: 

• M3 S<rpm> Turn on spindle on clockwise


• M5 Turn off spindle


• M4 S<rpm> Turn on spindle on counterclockwise


example: 

M3 S13000 

You can decide how fast the motor turn with this command: 

M3 S<rpm> where <rpm> can vary between 7000 to 14000 rpm (if you use a value lower than 7000 the spindle will not start). 

Use M3 command for standard mills (that are the most used), and M4 for counterclockwise mills (used just for special uses). 

millbit.jpgFor this mill use M3 millbit_counter.jpgFor this mill use M4 

Preflight check


1. Check if the bit is correctly fastened to the spindle 



2. Move slowly the carriage with the head inserted in its working position where can turn without touching anything. 



3. To check if everything is correctly working copy and paste this Gcode in the “Jog” 

M3 S7000 ;start spindle 7000 rpm  
G4 S5 ;pause 5 seconds 
M5 ;switch off spindle 




4. If eveything is working ok try to increase spin speed copy and paste this Gcode in the “Jog” 

M3 S14000 ;start spindle 14000 rpm 
 G4 S5 ;pause 5 seconds 
M5 ;switch off spindle

  
spindle.txt · Last modified: 2015/10/29 11:54 by jj
 
--------------------------------------------------------------------------------
