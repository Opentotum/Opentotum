hello_world_cnc

 
Hello world! (CNC milling)


Here you will be introduced to your first milling project. 

In this tutorial we are goint to explain how to use the FABtotum for CNC milling. 

We will engrave our claim “Make more” on a foam stock. You can donwload the SVG on wich the gcode is created. 

download.fabtotum.com/gcodes/milling/MakeMore.svg 

Download the .nc file (is the numerical control file, the .gcode for milling) 

download.fabtotum.com/gcodes/milling/MakeMore.nc 

If you want to learn how to create your own machining Gcodes, look at your CAD/CAM software package and follow the gcode guidelines. 

1. Turn around the hybrid bed so that shows the milling side. 




2. Place a piece of material that you will mill and fasten it to the bed (Using M4 Bolts and nuts or duct tape). 
 For the first tests would be better to use a soft and light material, like foam. 



3. Be careful: the stock material have to be positioned parallel to the X-Y axis.parallel.jpg 




4. For this example, the dimensions have to be at least 135x55x20mm (about 5x2x1 inch). 
measure_stock.jpg 




5. Remove the hybrid head head and using the provided tools install the milling bit of your choice.


6. Assemble the head on the carriage


7. Upload the .nc file in “Object manager”


8. Decide the “Zero point” on the stock material and mark it with a pen. The point hasn't to be exactly on the edge, but 3-4 mm centered. 
zero_right.jpg


9. In FABUI set the “Zero position” by moving the x,y and z axis (move this axis slowly, by reducing the “feedrate” and the “Z step” for not damage the tip). The tip have to be few microns from the stock material, for make a fine calibration you can use a piece of paper: position it over the stock material and start to raise the z axis slowly, start to move the paper until it reamin blocked between the tip and the stock material. 
 NOTICE: If the endtops get pressed click on the warning message “OK” and move the hybrid head by hand (If they remain pressed, the controls wouldn't work). 



10. When the tip is in the correct position, set “Zero” by clicking on the central button, then press “Start” this will “Zero” the position of the tool so it will start according the CAD drawing and more precisely aligned to the stock as the CAM instructions (gcode) expects. 




11. Press start. The milling motor will power up and the milling process will begin in seconds.start_milling.jpg


12. Wait for the milling process (less than 10 minutes).Take your time to go around in the Control tabs and see the current speed and RPMs. You can play around a bit if you are using Foam. Other materials will be less permissive.milling_finished.jpg


13. After a while the unnit will turn green and the tool will stop 
 .


14. Congratulations! You just milled your first object with your FABtotum.

  
hello_world_cnc.txt · Last modified: 2016/03/09 15:23 by jj