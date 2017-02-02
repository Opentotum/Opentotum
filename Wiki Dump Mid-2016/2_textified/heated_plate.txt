

heated_plate

  

Table of Contents


•Hybrid bed

◦Heated bed

◾Versions


◾Tech specs



◦Plateconn

◾V1


◾V2



◦

◾V2 BED Updating



◦Bed cleaning


◦


◦


◦CNC building plate:


 
Hybrid bed


The bed supplied with the FABtotum is classified as hybrid because it's composed by an heated bed, used during printing, and a milling plate used while CNC milling. 

To change from one kind of bed to the other one, just reverse it. 

If you have problems with the hybrid bed, check the trouble shooting page. 

Heated bed


The heated bed is an useful feature offered on the FABtotum: it improve the adherence and the reliability of the print, it's the first solution for get your prints to stick to the bed. 

Using Heated bed you won't need to use kapton tape or other tape, we just raccomend to use hair spray. 

Hair spray is made with polymers similar to the polymers used in 3D printing, so they will combine and stick perfectly, and when it's heated at least at 40 °C, it starts to melt and be sticky (look for the worst quality for the hairs and the strong hold, because it means it will stick stronger). 

Set these values on your slicing software: 

- For PLA:  0 - 60 °C (bed could be cold); 

- For ABS: 80 - 110 °C (The maximum reachable temperature depends on environment temperature) 

Versions


The hybrid bed is available in two different versions: the first version and a second version (released in late 2015) with stronger connection pins, heavier pcb routes, providing a faster heating and an improved reilability. 

bed_versions1.jpg 

 

V2 Hybrid bed (Printing side) 

Tech specs


Voltage source: 24 V 

Maximum Current: 6 A 

Maximum power: 144 W 

The glass is a Sodium calcium glass, must resist temps up to 130c. 

Dimensions: 228x244x3mm, all 4 sides are grinded. 

There are 4 red leds, switched on when the bed temperature is over 55°C. 

WARNING : Be careful don't damage the connection pins when inserting the printing bed. Insert the bed with the upper left corner first, then the upper right corner, and then the two lower corners. 

bed_on.jpg 

Plateconn



V1


connector_plate_pinout.jpg 

The first connector can be used for the 5th axis. It's controlled by the FABlin using the variable E1. 

V2




 

The V2 plateconn has the same pinout with bigger pads. They give a safer connection between the plate and the plateconn, giving more accurate temperatures and avoiding false contacts. 

V2 BED Updating


\\ Here you can find the tutorial how to update your bed. 

Bed cleaning




(Under construction) 



CNC building plate:


By overturning the heated bed you will have a building plate designed to be used for CNC milling. 

There are many holes used to fasten the parts to the bed using M4 nuts and bolts. 

WARNING: Insert the bolt head and fasten the stock using the nut, doing the opposite you could break the pcb. 

 
  
heated_plate.txt · Last modified: 2016/05/05 17:55 by jj
 
--------------------------------------------------------------------------------
