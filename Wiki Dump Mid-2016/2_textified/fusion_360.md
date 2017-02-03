

fusion_360

 
Fusion 360 CAM Setting


(Page under construction) 

With Autodesk Fusion 360 (Here you can download the free trial) there is an useful utility for generate CAM gcodes. 

• Model your object using the “Model” section (you can also import files modeled with other programs).


• Go to “CAM” section 



• Click on “Setup”: Here You can setup the origin, the orientation, the dimensions of on the stock. 
 In this section be careful the zero point have to be on the left-bottom corner, and the “Z” direction have to be concordant to the z direction of the printer (the tip of the arrow is where the bit enters). 



• Generate the toolpaths. You can choose to create 2D or 3D paths. In this case was generated a 3D path “Parallel”. 
Select the tool from the list or generate a new one


• After you generate toolpaths you have to postprocess the gcode.


• Download the FABtotum's CAM postprocessor Here


• Unzip it and copy the .cps file in Fusion 360's folder. 
 Path for Win: C:\Users\{username}\AppData\Local\Autodesk\webdeploy\production\{randomID}\Applications\CAM360\Data\Posts 
 Path for Mac: Macintosh HD ▸ Applica ▸ Fusion360 ▸ Contents ▸ Libraries ▸ Applications ▸ CAM360 ▸ Data ▸ Posts

  
fusion_360.txt · Last modified: 2015/07/16 19:12 by lux
 
--------------------------------------------------------------------------------
