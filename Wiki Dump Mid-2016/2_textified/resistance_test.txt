

resistance_test

  

Table of Contents


•Head resistance and thermistor testing


•

◦Purpose


◦What you need:


◦Procedure


◦Results


 
Head resistance and thermistor testing





Purpose


If your FABtotum’s head is not heating could happened that the heating resistance is damaged or somebody is wrong. With this tutorial you can know exactly which problem has your FABtotum. 

What you need:


• FABtotum head (V1 hybrid or V2 printing)


• Multimeter (electric tester, both analog or digital it’s ok) 




Procedure


1. Remove the head from the carriage, (doesn’t matter if you can’t remove the bowden tube).


2. Set the tester in resistance mode. If your multimeter has only one value set it in resistance mode, in some testers it’s indicated with the greek letter ohm (Ω). If it has more values related to ohms you should, when testing the resistor, set it to Ohm, when testing the thermistor set it to KOhm. 




3. Measure the resistance of the heating element: put the multimeter leads on the indicated points (From Left, pin 7 and 8 for the heater, 19 and 20 for the thermistor). It doesn’t matter which one is measured with the red or black leads: resistors and thermistors don’t have a polarity. 



Results


1. If you are measuring the heating element (resistor) you should measure a value between 12/16 Ohm (depending on environmental temperature, ecc). If you get infinite resistance (or OL, open loop), it means the resistor is not connected, if you measure 0 ohm, there is a shortcircuit somewhere in the head. 




2. If you are measuring the thermistor you should measure a value around 100K ohm (at 20°C), if you heat the hot end touching with the finger, you should see the resistance value decreasing. 



  
resistance_test.txt · Last modified: 2016/07/29 11:29 by fabtotum
 
--------------------------------------------------------------------------------
