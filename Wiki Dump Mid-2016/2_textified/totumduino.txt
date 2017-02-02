totumduino

  

Table of Contents


•Totumduino
◦ 
◾Features


◾Firmware



 
Totumduino




Totumduino is the name of the FABtotum Controller Board based on Arduino 

totumduino.jpg 

Features


• 4 axis connector


• 5th axis on a 4pole JST connector PH series 2mm connector


• Endstop n1


• Raspi GPIO header connector


• Hotbed connection


• emergency switch


• Case-door safety switch


• Front door safety switch


• YZ Endstops


• 24 v Power supply


• interior light output


• Second Extruder temp


• Head connector (this includes: Milling motor control, Extruder 1 heat control, Servo control, Servo powering, Laser control & power, Head light power, probe input,fan control and an I2C bus, X endstops, led controls.


• Board Fan power


Firmware


The Totumduino firmware is based on the Marlin firmware. The Totumduino firware source code can be found on GitHub at https://github.com/FABtotum/FABlin. 

Communications from the Raspberry Pi to the Totumduino uses a custom set of supported G-code. The G-code interpreter on the Totumduino interprets the commands into appropriate motion control actions. 
  
totumduino.txt · Last modified: 2015/07/03 10:58 by jj