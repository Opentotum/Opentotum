

mantainance

  

Table of Contents


•Maintenance

◦Head installing


◦


◦


◦Spool: loading and unloading

◾Loading


◾Unloading



◦Bed calibration

◾Printable addon for bed calibration



◦Probe calibration


◦First Setup


◦System info


◦


◦Cleaning the nozzle

◾Atomic method



◦Cleaning the feeder


 
Maintenance



Head installing


Since the introduction of the new V2 Head, from the FABUI 0.9495 is necessary to install the head on the FABUI to make the FABtotum recognize wich head is installed. 


In the “ FABUI”, go to “ Maintenance”, and choose “Head” for start the guided procedure. 


 

 

Choose the head you installed on your FABtotum choosing between: 

• Hybrid Head


• Printing head V2


• Milling head V2


 Warning:  selecting a wrong head you may damage both head and FABtotum. 

Spool: loading and unloading


This is the guided procedure for load and unload the 3D printing filament from your FABtotum. You will need to remove the filament also every time you are launching a rotational scan, 

Loading


in the “FABUI”, go to “Maintenance”, “Spool”, “Load spool” for start the guided procedure. 

 

 

1. Open the right compartment of your FABtotum


2. Cut the filament, making a sharpened tip


3. Insert the filament in the PTFE pipe until you reach the feeder (it becomes hard)


4. Wait until some plastic is coming out from the nozzle.


Unloading


In the “ FABUI”, go to “ Maintenance”, “ Spool”, “ Unload spool” for start the guided procedure. 

 

1. Wait for the nozzle reach the melting temperature


2. When you have reached the temperature, remove the bowden by pushing on the pushfit and pulling out the bowden 
removing_bowden.jpg


3. Cut the exceeding molten filament (if you don't it can get stuck in the bowden)


4. Open the right compartment


5. Press “Start” to unload the filament


Bed calibration


It's very important to have a planar printing bed for make the first printing layer stick perfectly. 
 With your FABtotum you can easily calibrate it using the guided procedure. 

1. In the “FABUI” go to “Maintenance” select “Bed calibration”. 




2. You will see the bed calibration wizard. Press Start for start the process. 



3. Wait for your printer starts to make the measure of the flatness of the bed in 4 different points. After few minutes you will see a screen like this: 



4. By working with the supplied allen key, rotate the screws that sustain the bed as the program tells you. 

regulating_bed.jpg


5. Repeat the measure, until you will see a screen like this:


6. Don't worry if the wizard says you have to turn for few degrees, the important is that every screw is green (Consider that every complete turn, you will raise or lower only for 0.5mm).


Congratulations! You just calibrated well the bed of your FABtotum printer. 

Printable addon for bed calibration


You can download and print a very useful tool to know exaclty how many degrees you rotated the screws. 

Download link: Thingiverse 

bed_leveling_tool.jpg 

Probe calibration


1. In the “FABUI” go to “maintenance” menu and select “Probe calibration” 




2. Now you can choose the assisted calibration or fine calibration.


3. Choosing the “Assisted calibration”, will start the assisted calibration.


4. Wait until the nozzle get hot (when i'ts hot it's longer due to thermal expansion).


5. Put a piece of copy paper (80 g/m2). Wait for the probe exit from his housing.


6. Move the paper adjusting the heigh by pressing “Z+” or “Z-” until it barely rubs against the nozzle, then press “Calibrate” 

probe_calibration_paper.jpg


First Setup


 

The first setup wizard is used for calibrate the FABtotum for the first use (in the factory every unit comes out calibrated, during shipping can happend the calibrations are lost). 

It contains the procedures for 

• Probe calibration


• Bed calibration


• Engaging feeder procedure (Only for the old versions, we suggest to follow the tutorial and update it to the new version).


 

System info


 

This section gives all the details about the FABtotum, like FABUI version, Firmware version, Installed head, etc. 

 



Cleaning the nozzle


1. From “jog” section in FABUI heat the nozzle to the melting material temperature (195°C for PLA, 225°C for ABS, etc).


2. Set feed rate for extrusion at 150 mm/min and extrude 10 mm of filament.


3. Continue extruding until the material is clean and flows good.


4. If you see sume burned material like ash, try this method


Atomic method


Atomic method is a good procedure for remove dust or burnt debris clogging the nozzle: it exploit the propriety of the thermoplastic who get sticky and hold the debris when they reach the glass transition temperature. 

1. From “jog” in FABUI heat the nozzle to the melting material temperature (195 for PLA 225 for ABS etc). 



2. Pull out the bowden from the head by pressing the pushfit, pull out the filamentremoving_bowden.jpg


3. Take a 20 cm piece of filament and push it inside the head (it could be difficult to center the hole without bowden) 

extruding_hand.jpg


4. Try to extrude a bit of material and then leave the filament there 

cleaning.jpg


5. Low down the temperature to the material glass transition temperature (60-65°C for PLA and 110-120° for ABS).


6. Wait for the temperature low down and pull out the material very slowly (be careful not break filament inside the extruder), if you can't pull out the material try to increase a little the temperature. 
 When the material comes out you could see some burnt material on the tip 

burnt.jpg


7. Repeat the whole method until you can see clean filament, if you are lucky you will see the tip with the plastic that was in the hole of the nozzle, like this: 

cleaned_nozzle.jpg


8. For further info check those websites (those links refers the Ultimaker 3D printer, which have a higher temperature reading of 20°C) 


ultimaker.com/en/support/view/149-atomic-method 
support.3dverkstan.se/article/10-the


Cleaning the feeder


Please see our feeder page. 
  
mantainance.txt · Last modified: 2016/05/13 14:39 by fabtotum
 
--------------------------------------------------------------------------------
